# apps/orders/webhook_handler.py

import json
import time
import logging

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

from .models import Order, OrderItem
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
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """Handle unexpected/unknown webhook events."""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe.
        Marks the Order paid and sends confirmation email.
        """
        intent = event['data']['object']
        pid = intent.get('id')
        metadata = intent.get('metadata', {})
        order_id = metadata.get('order_id')

        if not order_id:
            logger.warning("⚠️  No order_id in metadata for Intent %s", pid)
            return HttpResponse(status=200)

        try:
            order = Order.objects.get(pk=order_id, stripe_session_id=pid)
        except Order.DoesNotExist:
            logger.error("❌ Order %s with session %s not found", order_id, pid)
            return HttpResponse(status=200)

        # mark paid
        order.status = 'paid'
        order.save()
        logger.info("✅ Order %s marked PAID", order_id)

        # send the user a confirmation email
        self._send_confirmation_email(order)

        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | '
                     'SUCCESS: Payment processed for order'),
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe.
        """
        logger.info("⚠️  Payment failed: %s", event['data']['object'].get('id'))
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
