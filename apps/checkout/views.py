# apps/checkout/views.py

import json
import stripe
from decimal import Decimal

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import (
    HttpResponse, HttpResponseBadRequest, JsonResponse
)
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views import View
from django.views.generic import TemplateView

from ..trailer.models import Cart
from .models import Order, OrderLineItem
from .forms import OrderForm
from .webhooks import stripe_webhook  # move your webhook here

# initialize Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# decorator helper
login_req = method_decorator(login_required, name="dispatch")


@require_POST
@csrf_exempt
@login_required
def cache_checkout_data(request):
    """
    AJAX endpoint: attach order_id + save_info to the PaymentIntent
    before you do stripe.confirmCardPayment(...) in JS.
    """
    try:
        data = json.loads(request.body)
        pid  = data["client_secret"].split("_secret")[0]
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "order_id":  data.get("order_id"),
                "save_info": data.get("save_info", False),
            }
        )
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponseBadRequest(str(e))


@login_req
class CheckoutView(View):
    """
    GET → render your Stripe Elements checkout page
        (creates a PaymentIntent under the hood)

    POST → user has completed card entry & JS has succeeded →
        save shipping info on the Order and redirect to success.
    """
    template_name = "checkout/checkout.html"

    def get(self, request, order_id, *args, **kwargs):
        # 1) Lookup the Order & Cart
        order = get_object_or_404(Order, pk=order_id, user=request.user)
        cart  = Cart.objects.get(user=request.user)

        # Guard: cart must match order or be non-empty
        if not cart.items.exists() or order.total_amount < Decimal("1.00"):
            messages.error(request, "Your cart is empty or below £1.00 minimum.")
            return redirect("trailer:cart_detail")

        # 2) Create a PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount   = int(order.total_amount * Decimal("100")),
            currency = "gbp",
            metadata = {"order_id": order.pk},
        )

        # 3) Build line‐items for the template
        line_items = [
            {
                "name":     str(item.car),
                "quantity": item.quantity,
                "unit":     item.unit_price,
                "subtotal": item.line_total,
            }
            for item in order.items.select_related("car")
        ]

        return render(request, self.template_name, {
            "order":          order,
            "client_secret":  intent.client_secret,
            "stripe_pk":      settings.STRIPE_PUBLISHABLE_KEY,
            "line_items":     line_items,
            "product_count":  sum(i["quantity"] for i in line_items),
            "total":          order.total_amount,
            "delivery":       order.delivery_fee,
            "grand_total":    order.total_with_delivery,
        })

    def post(self, request, order_id, *args, **kwargs):
        # Save the shipping info from your JS form into the Order
        order = get_object_or_404(Order, pk=order_id, user=request.user)
        form  = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("checkout:success", order_id=order.pk)
        else:
            messages.error(request, "There was an error with your delivery info.")
            return redirect("checkout:checkout", order_id=order.pk)


@login_req
class CheckoutSuccessView(TemplateView):
    """
    GET → after a successful payment, show a thank you page.
    """
    template_name = "checkout/success.html"

    def get(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id, user=request.user)
        return render(request, self.template_name, {"order": order})


# re-export your webhook here so you can point core/urls.py at it
stripe_webhook = stripe_webhook
