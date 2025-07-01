# apps/orders/webhooks.py

import json
import logging

import stripe
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .webhook_handler import StripeWH_Handler

logger = logging.getLogger(__name__)

# Initialize Stripe with your secret key
stripe.api_key = settings.STRIPE_SECRET_KEY
ENDPOINT_SECRET = settings.STRIPE_WEBHOOK_SECRET


@csrf_exempt
@require_POST
def stripe_webhook(request):
    """
    Listen for Stripe webhooks, verify the signature, and
    dispatch to the appropriate handler method in StripeWH_Handler.
    """
    # 1) Retrieve the payload and Stripe signature header
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")

    logger.debug("🔍 Raw payload: %r", payload)
    logger.debug("🔑 Signature header: %s", sig_header)

    # 2) Verify webhook signature and construct the event
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, ENDPOINT_SECRET
        )
        logger.info("✅ Webhook verified: %s", event["type"])
    except ValueError as e:
        logger.error("❌ Invalid payload: %s", e)
        return HttpResponseBadRequest("Invalid payload")
    except stripe.error.SignatureVerificationError as e:
        logger.error("⚠️  Signature verification failed: %s", e)
        return HttpResponseBadRequest("Invalid signature")

    # 3) Instantiate your handler class
    handler = StripeWH_Handler(request)

    # 4) Map Stripe event types to your handler methods
    event_map = {
        "checkout.session.completed":     handler.handle_checkout_session_completed,
        "payment_intent.succeeded":       handler.handle_payment_intent_succeeded,
        "payment_intent.payment_failed":  handler.handle_payment_intent_payment_failed,
        # add other event → handler mappings here if needed
    }

    # 5) Get the correct handler or fall back to generic
    event_type = event["type"]
    event_handler = event_map.get(event_type, handler.handle_event)

    # 6) Call the handler with the event
    response = event_handler(event)
    return response
