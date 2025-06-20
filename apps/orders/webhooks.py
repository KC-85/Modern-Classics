# orders/webhooks.py

import json
import logging

import stripe
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Order

# set up logging
logger = logging.getLogger(__name__)

stripe.api_key = settings.STRIPE_SECRET_KEY
ENDPOINT_SECRET = settings.STRIPE_WEBHOOK_SECRET

@csrf_exempt
@require_POST
def stripe_webhook(request):
    # 1) Decode & log the raw payload
    payload = request.body.decode("utf-8")
    logger.debug("Stripe webhook payload: %s", payload)

    # 2) Grab signature header & log it
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")
    logger.debug("Stripe signature header: %s", sig_header)

    # 3) Try constructing the Event, catching parse or sig errors
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, ENDPOINT_SECRET
        )
        logger.info("Webhook verified, received event type: %s", event["type"])
    except ValueError as ve:
        logger.error("⚠️  Invalid payload: %s", ve)
        return HttpResponseBadRequest("Invalid payload")
    except stripe.error.SignatureVerificationError as se:
        logger.error("⚠️  Signature verification failed: %s", se)
        return HttpResponseBadRequest("Invalid signature")

    # 4) Handle the payment_intent.succeeded event
    if event["type"] == "payment_intent.succeeded":
        intent = event["data"]["object"]
        logger.debug("Handling payment_intent.succeeded for Intent ID: %s", intent["id"])

        pi_id = intent["id"]
        amount = intent["amount_received"]
        currency = intent["currency"]
        shipping = intent.get("shipping", {})
        metadata = intent.get("metadata", {})

        order_id = metadata.get("order_id")
        if not order_id:
            logger.warning("No order_id in metadata for Intent %s", pi_id)
        else:
            try:
                order = Order.objects.get(pk=order_id, stripe_intent_id=pi_id)
                order.status = Order.Status.PAID
                order.paid_amount = amount / 100
                order.currency = currency
                order.shipping_address = shipping.get("address", {})
                order.shipping_name = shipping.get("name")
                order.save()
                logger.info("Order %s marked PAID", order_id)
            except Order.DoesNotExist:
                logger.error("Order matching ID %s and Intent %s not found", order_id, pi_id)

    # 5) Always return HTTP 200 so Stripe knows we got it
    return HttpResponse(status=200)
