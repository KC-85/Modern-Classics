# apps/checkout/views.py

import json
import stripe
from decimal import Decimal

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from apps.common.auth_mixins import LoginRequiredMessageMixin
from apps.common.auth_mixins import login_required_with_message  # helper for FBVs

from .models import Order, OrderLineItem
from .forms  import OrderForm
from .webhooks import stripe_webhook
from ..trailer.models import Cart
from apps.showroom.models import Car
from .utils import compute_delivery

stripe.api_key = settings.STRIPE_SECRET_KEY


# ---------- FBVs ----------

@require_POST
@csrf_exempt
@login_required_with_message          # << show banner + redirect to login for guests
def cache_checkout_data(request):
    try:
        data = json.loads(request.body or "{}")
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


@require_POST
@login_required_with_message          # << and here too
def create_order(request):
    """
    Turn the current user’s Cart into an Order + line items,
    then send them on to the Stripe checkout step.
    """
    cart = get_object_or_404(Cart, user=request.user)

    if not cart.items.exists():
        messages.error(request, "Your cart is empty.")
        return redirect("trailer:cart_detail")

    order = Order.objects.create(
        user=request.user,
        original_trailer={"items": [
            {
                "car_id": ci.car_id,
                "name":   str(ci.car),
                "qty":    ci.quantity,
                "unit":   float(ci.car.price),
                "total":  float(ci.car.price * ci.quantity),
            } for ci in cart.items.select_related("car")
        ]},
    )

    for ci in cart.items.select_related("car"):
        OrderLineItem.objects.create(
            order=order,
            car=ci.car,
            quantity=ci.quantity,
            unit_price=ci.car.price,
        )

    # Optionally keep cart until payment succeeds via webhook; or clear now:
    # cart.items.all().delete()

    return redirect("checkout:checkout", order_id=order.pk)


# ---------- CBVs ----------

class CreateOrderView(LoginRequiredMessageMixin, View):
    def post(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, user=request.user)
        if not cart.items.exists():
            messages.error(request, "Your cart is empty.")
            return redirect("trailer:cart_detail")

        order = Order.objects.create(
            user=request.user,
            original_trailer={"items": [
                {
                    "car_id": ci.car_id,
                    "name":   str(ci.car),
                    "qty":    ci.quantity,
                    "unit":   float(ci.car.price),
                    "total":  float(ci.car.price * ci.quantity),
                } for ci in cart.items.select_related("car")
            ]},
            full_name="", email=request.user.email or "",
            phone_number="", country="", postcode="",
            town_or_city="", street_address1="", street_address2="", county="",
        )

        for ci in cart.items.select_related("car"):
            OrderLineItem.objects.create(
                order=order,
                car=ci.car,
                quantity=ci.quantity,
                unit_price=ci.car.price,
            )

        order.save()
        return redirect("checkout:checkout", order_id=order.pk)


class CheckoutView(LoginRequiredMessageMixin, View):
    template_name = "checkout/checkout.html"

    def get(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id, user=request.user)

        order.save()  # recompute order_total from lineitems
        order.delivery_cost = compute_delivery(order.order_total)
        order.save(update_fields=["delivery_cost"])
        order.save()  # recalculates grand_total

        intent = stripe.PaymentIntent.create(
            amount=int(order.grand_total * Decimal("100")),
            currency="gbp",
            metadata={"order_id": order.pk},
        )
        order.stripe_pid = intent.id
        order.save(update_fields=["stripe_pid"])

        line_items = [
            {
                "name":     str(li.car),
                "quantity": li.quantity,
                "unit":     li.unit_price,
                "subtotal": li.lineitem_total,
            }
            for li in order.lineitems.select_related("car")
        ]

        ctx = {
            "order":         order,
            "order_form":    OrderForm(instance=order),
            "line_items":    line_items,
            "total":         order.order_total,
            "delivery":      order.delivery_cost,
            "grand_total":   order.grand_total,
            "client_secret": intent.client_secret,
            "stripe_public": settings.STRIPE_PUBLISHABLE_KEY,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id, user=request.user)
        form = OrderForm(request.POST, instance=order)

        if not form.is_valid():
            line_items = [
                {
                    "name":     str(li.car),
                    "quantity": li.quantity,
                    "unit":     li.unit_price,
                    "subtotal": li.lineitem_total,
                }
                for li in order.lineitems.select_related("car")
            ]
            ctx = {
                "order":         order,
                "order_form":    form,
                "line_items":    line_items,
                "total":         order.order_total,
                "delivery":      order.delivery_cost,
                "grand_total":   order.grand_total,
                "client_secret": request.POST.get("client_secret", ""),
                "stripe_public": settings.STRIPE_PUBLISHABLE_KEY,
            }
            messages.error(request, "Please fix the errors in the form.")
            return render(request, self.template_name, ctx)

        form.save()
        return redirect("checkout:success", order_id=order.pk)


class OrderDetailView(LoginRequiredMessageMixin, View):
    template_name = "orders/order_detail.html"

    def get(self, request, order_number, *args, **kwargs):
        qs = (Order.objects
                    .filter(user=request.user)
                    .prefetch_related("lineitems", "lineitems__car"))
        order = get_object_or_404(qs, order_number=order_number)
        return render(request, self.template_name, {"order": order})


class CheckoutSuccessView(LoginRequiredMessageMixin, TemplateView):
    template_name = "checkout/success.html"

    def get(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id, user=request.user)
        return render(request, self.template_name, {"order": order})


class OrderHistoryView(LoginRequiredMessageMixin, ListView):
    model               = Order
    template_name       = "checkout/order_list.html"
    context_object_name = "orders"
    paginate_by         = 10

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-date")

