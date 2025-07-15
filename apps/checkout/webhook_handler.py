# apps/orders/webhook_handler.py

import json
import logging
from decimal import Decimal

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

from .models import Order, OrderLineItem
from apps.showroom.models import Car

logger = logging.getLogger(__name__)
User = get_user_model()


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email."""
        cust_email = order.user.email
        subject = render_to_string(
            'orders/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        ).strip()
        body = render_to_string(
            'orders/confirmation_emails/confirmation_email_body.txt',
            {
                'order': order,
                'contact_email': settings.DEFAULT_FROM_EMAIL
            }
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email],
            fail_silently=False
        )

    def handle_event(self, event):
        """Fallback handler for unexpected/unknown webhook events."""
        logger.warning(f"Unhandled webhook event received: {event['type']}")
        return HttpResponse(status=200)

    def handle_checkout_session_completed(self, event):
        """
        Handle the checkout.session.completed webhook from Stripe.
        1) Retrieve the session object
        2) Extract order_id from session.metadata
        3) Mark that Order as PAID, set paid_amount & currency
        4) Send confirmation email
        """
        session = event['data']['object']
        metadata = session.get('metadata', {})
        order_id = metadata.get('order_id')

        if not order_id:
            logger.error("🔴 checkout.session.completed missing order_id in metadata")
            return HttpResponse(status=400)

        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            logger.error(f"🔴 Order {order_id} not found for checkout.session.completed")
            return HttpResponse(status=404)

        if order.status == Order.Status.PENDING:
            order.status      = Order.Status.PAID
            order.paid_amount = Decimal(session['amount_total']) / 100
            order.currency    = session['currency'].upper()
            order.save(update_fields=['status', 'paid_amount', 'currency'])
            logger.info(f"✅ Order {order_id} marked PAID via checkout.session.completed")

            # Send the confirmation email
            self._send_confirmation_email(order)

        return HttpResponse(status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe.
        Marks the Order paid and sends confirmation email.
        """
        intent   = event['data']['object']
        pid      = intent.get('id')
        metadata = intent.get('metadata', {})
        order_id = metadata.get('order_id')

        if not order_id:
            logger.warning(f"⚠️  payment_intent.succeeded missing order_id for Intent {pid}")
            return HttpResponse(status=200)

        try:
            order = Order.objects.get(pk=order_id, stripe_session_id=pid)
        except Order.DoesNotExist:
            logger.error(f"❌ Order {order_id} with session {pid} not found")
            return HttpResponse(status=200)

        if order.status == Order.Status.PENDING:
            order.status = Order.Status.PAID
            order.save(update_fields=['status'])
            logger.info(f"✅ Order {order_id} marked PAID via payment_intent.succeeded")

            # Send the confirmation email
            self._send_confirmation_email(order)

        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | '
                     f'SUCCESS: PaymentIntent {pid} processed for order {order_id}'),
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe.
        """
        intent_id = event['data']['object'].get('id')
        logger.info(f"⚠️  Payment failed for PaymentIntent {intent_id}")
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
