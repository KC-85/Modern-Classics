# apps/checkout/webhook_handler.py
import logging
from decimal import Decimal

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils import timezone

from .models import Order

logger = logging.getLogger(__name__)


class StripeWH_Handler:
    """
    Handle Stripe webhooks for the Modern Classics checkout app.
    Assumes PaymentIntent metadata includes {"order_id": <order.pk>}.
    """

    def __init__(self, request):
        self.request = request

    # ----------------------------- helpers -----------------------------

    def _send_confirmation_email(self, order: Order) -> None:
        """
        Send a simple text receipt using:
        templates/checkout/confirmation_emails/{subject.txt, body.txt}
        """
        to_email = order.email or (order.user.email if order.user else "")
        if not to_email:
            logger.warning("Order %s has no email; skipping receipt", order.pk)
            return

        subject = render_to_string(
            "checkout/confirmation_emails/subject.txt",
            {"order": order},
        ).strip()

        body = render_to_string(
            "checkout/confirmation_emails/body.txt",
            {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
        )

        send_mail(
            subject=subject,
            message=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[to_email],
            fail_silently=False,
        )

    # -------------------------- generic fallback -----------------------

    def handle_event(self, event):
        """
        Fallback for unhandled event types. Always return 200 so Stripe
        won’t keep retrying forever on unknown events.
        """
        logger.warning("Unhandled webhook event type: %s", event.get("type"))
        return HttpResponse(status=200)

    # ---------------------------- key events ---------------------------

    def handle_payment_intent_succeeded(self, event):
        intent   = event["data"]["object"]
        pid      = intent.get("id")
        metadata = intent.get("metadata") or {}
        order_id = metadata.get("order_id")

        if not order_id:
            return HttpResponse(status=200)

        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return HttpResponse(status=200)

        # Persist PI id if not recorded yet
        if pid and not order.stripe_pid:
            order.stripe_pid = pid

        # Stripe amounts are in the smallest unit (pence); prefer amount_received
        amt = intent.get("amount_received") or intent.get("amount")
        if amt is not None and hasattr(order, "paid_amount"):
            order.paid_amount = Decimal(amt) / Decimal("100")

        if intent.get("currency") and hasattr(order, "currency"):
            order.currency = intent["currency"].upper()

        if hasattr(order, "status"):
            order.status = Order.PaymentStatus.PAID
        if hasattr(order, "paid_at"):
            order.paid_at = timezone.now()

        # Save only fields that exist on your model
        fields_to_update = ["stripe_pid"]
        for f in ("paid_amount", "currency", "status", "paid_at"):
            if hasattr(order, f):
                fields_to_update.append(f)
        order.save(update_fields=fields_to_update)

        # (Optional) mark cars sold & clear from other carts here if you added that logic

        self._send_confirmation_email(order)
        return HttpResponse(status=200)

    def handle_payment_intent_payment_failed(self, event):
        intent   = event["data"]["object"]
        metadata = intent.get("metadata") or {}
        order_id = metadata.get("order_id")

        if order_id:
            try:
                order = Order.objects.get(pk=order_id)
            except Order.DoesNotExist:
                return HttpResponse(status=200)
            if hasattr(order, "status"):
                order.status = Order.PaymentStatus.FAILED
                order.save(update_fields=["status"])

        return HttpResponse(status=200)

    # ---------------------- optional: Checkout Session ------------------

    def handle_checkout_session_completed(self, event):
        """
        Only used if you switch to Stripe Checkout Sessions (hosted page).
        """
        session  = event["data"]["object"]
        metadata = session.get("metadata") or {}
        order_id = metadata.get("order_id")

        if not order_id:
            return HttpResponse(status=200)

        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return HttpResponse(status=200)

        self._send_confirmation_email(order)
        logger.info("Receipt sent for order %s (checkout.session.completed)", order.pk)
        return HttpResponse(status=200)
