"""Webhook endpoint handlers for the checkout app.

Accepts external service callbacks and delegates event processing."""

# apps/checkout/webhooks.py
import logging
import stripe

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .webhook_handler import StripeWH_Handler

logger = logging.getLogger(__name__)

stripe.api_key = settings.STRIPE_SECRET_KEY
WH_SECRET = settings.STRIPE_WEBHOOK_SECRET


@csrf_exempt
def stripe_webhook(request):
    # 1) Verify signature & construct event from the *raw* body
    payload = request.body  # <-- keep raw bytes
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, WH_SECRET)
    except ValueError as err:
        logger.warning("Stripe webhook: invalid JSON payload (%s)", err)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as err:
        logger.warning("Stripe webhook: invalid signature (%s)", err)
        return HttpResponse(status=400)
    except Exception as err:
        logger.error("Stripe webhook: unexpected error (%s)", err)
        return HttpResponse(status=400)

    logger.info("Stripe webhook received: id=%s type=%s",
                event.get("id"), event.get("type"))

    # 2) Dispatch
    handler = StripeWH_Handler(request)
    event_map = {
        "payment_intent.succeeded": handler.handle_payment_intent_succeeded,
        "payment_intent.payment_failed": (
            handler.handle_payment_intent_payment_failed
        ),
        "checkout.session.completed": (
            handler.handle_checkout_session_completed
        ),
    }
    fn = event_map.get(event.get("type"), handler.handle_event)
    return fn(event)
