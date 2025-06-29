# apps/orders/webhooks.py

import json
import logging

import stripe
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Order
from .webhook_handler import StripeWH_Handler

# set up logging
logger = logging.getLogger(__name__)

# configure Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
ENDPOINT_SECRET = settings.STRIPE_WEBHOOK_SECRET

@csrf_exempt
@require_POST
def stripe_webhook(request):
    """
    Listen for Stripe webhooks, verify signature, then
    dispatch to the appropriate handler method in StripeWH_Handler.
    """
    # 1) Raw payload & signature header
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")

    logger.debug("🔍 Raw payload (bytes): %r", payload)
    logger.debug("🔑 Stripe signature header: %s", sig_header)
    logger.debug("🔑 Using endpoint secret: %r", ENDPOINT_SECRET)

    # 2) Verify signature & construct event
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, ENDPOINT_SECRET
        )
        logger.info("✅ Webhook verified, received event type: %s", event["type"])
    except ValueError as e:
        logger.error("❌ Invalid payload: %s", e)
        return HttpResponseBadRequest("Invalid payload")
    except stripe.error.SignatureVerificationError as e:
        logger.error("⚠️  Signature verification failed: %s", e)
        return HttpResponseBadRequest("Invalid signature")

    # 3) Set up handler
    handler = StripeWH_Handler(request)

    # 4) Map event types to handler methods
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
        # add additional event mappings here as you implement them:
        # 'charge.refunded': handler.handle_charge_refunded,
    }

    # 5) Lookup & invoke the correct handler, fallback to generic
    event_type = event['type']
    event_handler = event_map.get(event_type, handler.handle_event)
    response = event_handler(event)

    # 6) Return whatever the handler returns (should be an HttpResponse)
    return response

