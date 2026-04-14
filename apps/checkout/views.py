"""View logic for the checkout app.

Handles HTTP requests, orchestrates domain operations, and returns rendered responses."""

# apps/checkout/views.py

# Python first
import json
import stripe
from decimal import Decimal

# Django second
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import transaction
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Own files last
from .utils import compute_delivery
from apps.showroom.models import Car
from ..trailer.models import Cart
from .webhooks import stripe_webhook
from .forms import OrderForm
from .models import Order, OrderLineItem
from apps.common.auth_mixins import login_required_with_message
from apps.common.auth_mixins import LoginRequiredMessageMixin

stripe.api_key = settings.STRIPE_SECRET_KEY


# ---------- FBVs ----------

@require_POST
@csrf_exempt
# << show banner + redirect to login for guests
@login_required_with_message
def cache_checkout_data(request):
    try:
        data = json.loads(request.body or "{}")
        pid = data["client_secret"].split("_secret")[0]
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
@transaction.atomic
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
    @transaction.atomic
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

        intent = None
        if order.stripe_pid:
            try:
                intent = stripe.PaymentIntent.retrieve(order.stripe_pid)
            except Exception:
                intent = None

        if intent and intent.get("status") == "succeeded":
            order.status = Order.PaymentStatus.PAID
            amount = intent.get("amount_received") or intent.get("amount")
            if amount is not None:
                order.paid_amount = Decimal(amount) / Decimal("100")
            currency = intent.get("currency")
            if currency:
                order.currency = currency.upper()
            if not order.paid_at:
                order.paid_at = timezone.now()
            order.save(update_fields=["status", "paid_amount", "currency", "paid_at"])
            return redirect("checkout:success", order_id=order.pk)

        if not intent:
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

        client_secret = getattr(intent, "client_secret", None)
        if client_secret is None and hasattr(intent, "get"):
            client_secret = intent.get("client_secret", "")

        ctx = {
            "order":         order,
            "order_form":    OrderForm(instance=order),
            "line_items":    line_items,
            "total":         order.order_total,
            "delivery":      order.delivery_cost,
            "grand_total":   order.grand_total,
            "client_secret": client_secret,
            "stripe_public": settings.STRIPE_PUBLISHABLE_KEY,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id, user=request.user)
        form = OrderForm(request.POST, instance=order)

        def _checkout_context(order_obj, order_form, client_secret_value):
            line_items = [
                {
                    "name":     str(li.car),
                    "quantity": li.quantity,
                    "unit":     li.unit_price,
                    "subtotal": li.lineitem_total,
                }
                for li in order_obj.lineitems.select_related("car")
            ]
            return {
                "order":         order_obj,
                "order_form":    order_form,
                "line_items":    line_items,
                "total":         order_obj.order_total,
                "delivery":      order_obj.delivery_cost,
                "grand_total":   order_obj.grand_total,
                "client_secret": client_secret_value,
                "stripe_public": settings.STRIPE_PUBLISHABLE_KEY,
            }

        if not form.is_valid():
            ctx = _checkout_context(order, form, request.POST.get("client_secret", ""))
            messages.error(request, "Please fix the errors in the form.")
            return render(request, self.template_name, ctx)

        form.save()

        # Server-side confirmation of payment keeps status accurate even
        # when webhook delivery is delayed or misconfigured.
        client_secret = request.POST.get("client_secret", "")
        pid = client_secret.split("_secret")[0] if "_secret" in client_secret else ""
        if not pid:
            messages.error(request, "Payment could not be verified. Please try again.")
            ctx = _checkout_context(order, form, client_secret)
            return render(request, self.template_name, ctx)

        try:
            intent = stripe.PaymentIntent.retrieve(pid)
        except Exception:
            intent = None

        if not intent or intent.get("status") != "succeeded":
            messages.error(request, "Payment was not completed. Your order remains pending.")
            ctx = _checkout_context(order, form, client_secret)
            return render(request, self.template_name, ctx)

        order.status = Order.PaymentStatus.PAID
        amount = intent.get("amount_received") or intent.get("amount")
        if amount is not None:
            order.paid_amount = Decimal(amount) / Decimal("100")
        currency = intent.get("currency")
        if currency:
            order.currency = currency.upper()
        order.paid_at = timezone.now()
        order.save(update_fields=["status", "paid_amount", "currency", "paid_at"])

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

    def send_receipt(self, order):
        """Send the same receipt the webhook used to send."""
        if getattr(order, "status", None) != Order.PaymentStatus.PAID:
            return False

        # Treat already-fulfilled orders as no-op so refreshing success page
        # does not resend emails or re-run fulfillment logic.
        existing_cart = Cart.objects.filter(user=self.request.user).first()
        all_items_already_sold = all(
            line_item.car.is_sold for line_item in order.lineitems.select_related("car")
        )
        if not existing_cart and all_items_already_sold:
            return False

        to_email = order.email or (order.user.email if order.user else "")

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

        # Mark all cars in this order as is_sold=True
        for line_item in order.lineitems.select_related("car"):
            car = line_item.car
            car.is_sold = True
            car.save(update_fields=["is_sold"])

        # Delete the user's cart upon successful purchase
        cart = existing_cart
        if not cart:
            return False
        cart.delete()
        return True

    def get(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id, user=request.user)
        if getattr(order, "status", None) != Order.PaymentStatus.PAID:
            messages.error(request, "Payment is not complete yet. Please try checkout again.")
            return redirect("checkout:checkout", order_id=order.pk)

        self.send_receipt(order)
        return render(request, self.template_name, {"order": order})


class OrderHistoryView(LoginRequiredMessageMixin, ListView):
    model = Order
    template_name = "checkout/order_list.html"
    context_object_name = "orders"
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-date")
