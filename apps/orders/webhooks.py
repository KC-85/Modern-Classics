# orders/webhooks.py

import stripe
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY
ENDPOINT_SECRET = settings.STRIPE_WH_SECRET

@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, ENDPOINT_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponseBadRequest("Invalid payload or signature")

    # Only handle successful charges
    if event["type"] == "payment_intent.succeeded":
        intent = event["data"]["object"]  # the PaymentIntent
        pi_id = intent["id"]
        amount = intent["amount_received"]
        currency = intent["currency"]
        shipping = intent.get("shipping", {})
        metadata = intent.get("metadata", {})

        # We stored our internal order PK in metadata['order_id']
        order_id = metadata.get("order_id")
        if order_id:
            try:
                order = Order.objects.get(pk=order_id, stripe_intent_id=pi_id)
                order.status = Order.Status.PAID
                order.paid_amount = amount / 100  # convert cents ⇒ dollars
                order.currency = currency
                # Optionally store shipping info:
                order.shipping_address = shipping.get("address", {})
                order.shipping_name = shipping.get("name")
                order.save()
            except Order.DoesNotExist:
                # log: no matching order
                pass

    # You can handle other event types here (refunds, disputes, etc.)

    return HttpResponse(status=200)
