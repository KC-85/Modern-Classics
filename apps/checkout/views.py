# apps/checkout/views.py

import json
import stripe
from decimal import Decimal

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views import View
from django.views.generic import TemplateView, ListView

from .models import Order, OrderLineItem
from .forms  import OrderForm
from .webhooks import stripe_webhook     # your webhook entry‐point
from ..trailer.models import Cart
from apps.showroom.models import Car     # so you can look up cars

# initialize Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# helper to decorate CBVs
login_req = method_decorator(login_required, name="dispatch")

@login_required
@require_POST
def create_order(request):
    """
    Turn the current user’s Cart into an Order + line items,
    then send them on to the Stripe checkout step.
    """
    cart = get_object_or_404(Cart, user=request.user)

    if not cart.items.exists():
        messages.error(request, "Your cart is empty.")
        return redirect("trailer:cart_detail")

    # Create the Order
    order = Order.objects.create(
        user=request.user,
        original_trailer=cart,
        # you can prefill other Order fields (like full_name/email) here if you want
    )

    # Convert each Cart item into an OrderLineItem
    for cart_item in cart.items.select_related("car"):
        OrderLineItem.objects.create(
            order=order,
            car=cart_item.car,
            quantity=cart_item.quantity,
            unit_price=cart_item.unit_price,
        )

    # (Optional) Clear the cart now that it’s in the order:
    cart.items.all().delete()

    # Redirect into your existing CheckoutView,
    #    which expects an order_id URL kwarg:
    return redirect("checkout:checkout", order_id=order.pk)

@require_POST
@csrf_exempt
@login_required
def cache_checkout_data(request):
    """
    AJAX endpoint: attach order_id + save_info to the PaymentIntent
    before stripe.confirmCardPayment(...) in your JS.
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
class CreateOrderView(View):
    def post(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, user=request.user)
        if not cart.items.exists():
            messages.error(request, "Your cart is empty.")
            return redirect("trailer:cart_detail")

        # 1) Snapshot from Car.price (never CartItem.unit_price)
        cart_snapshot = []
        for ci in cart.items.select_related("car"):
            price = ci.car.price
            qty   = ci.quantity
            cart_snapshot.append({
                "car_id":     ci.car.id,
                "car_name":   str(ci.car),
                "quantity":   qty,
                "unit_price": float(price),
                "line_total": float(price * qty),
            })

        # 2) Draft order (shipping saved on checkout page)
        order = Order.objects.create(
            user=request.user,
            original_trailer=cart_snapshot,
            full_name="", email=request.user.email or "",
            phone_number="", country="", postcode="",
            town_or_city="", street_address1="", street_address2="", county="",
        )

        # 3) Line items (again, price from Car.price)
        for ci in cart.items.select_related("car"):
            OrderLineItem.objects.create(
                order=order,
                car=ci.car,
                quantity=ci.quantity,
                unit_price=ci.car.price,
            )

        # 4) Recalc totals (your Order.save() computes from lineitems)
        order.save()

        # 5) Don’t clear cart here; do it after payment succeeds
        return redirect("checkout:checkout", order_id=order.pk)


@login_req
class CheckoutView(View):
    template_name = "checkout/checkout.html"

    def get(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id, user=request.user)

        # Recalc totals from lineitems (your Order.save() does this)
        order.save()

        # Create PaymentIntent for the grand total (pennies)
        amount_pennies = int(order.grand_total * Decimal("100"))
        intent = stripe.PaymentIntent.create(
            amount=amount_pennies,
            currency="gbp",
            metadata={"order_id": order.pk},
        )
        order.stripe_pid = intent.id
        order.save(update_fields=["stripe_pid"])

        # Build rows for the template from OrderLineItem
        line_items = [
            {
                "name":     str(li.car),
                "quantity": li.quantity,
                "unit":     li.unit_price,
                "subtotal": li.lineitem_total,
            }
            for li in order.lineitems.select_related("car")
        ]

        context = {
            "order":         order,
            "order_form":    OrderForm(instance=order),
            "line_items":    line_items,
            "total":         order.order_total,     # ← not total_amount
            "delivery":      order.delivery_cost,
            "grand_total":   order.grand_total,
            "client_secret": intent.client_secret,
            "stripe_public": settings.STRIPE_PUBLISHABLE_KEY,
        }
        return render(request, self.template_name, context)

    def post(self, request, order_id, *args, **kwargs):
        """Save shipping/contact after Stripe confirms in the browser."""
        order = get_object_or_404(Order, pk=order_id, user=request.user)

        form = OrderForm(request.POST, instance=order)
        if not form.is_valid():
            messages.error(request, "Please fix the errors in the form.")
            return redirect("checkout:checkout", order_id=order.pk)

        form.save()

        # (Optional) quick server-side sanity check of the PI
        cs = request.POST.get("client_secret", "")
        if "_secret" in cs:
            pid = cs.split("_secret")[0]
            try:
                pi = stripe.PaymentIntent.retrieve(pid)
                if pi.status != "succeeded":
                    messages.error(request, "Payment not confirmed yet.")
                    return redirect("checkout:checkout", order_id=order.pk)
            except Exception:
                # If you rely on the webhook as the source of truth, you can ignore errors here.
                pass

        # Clear the cart now that payment + details are good
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart.items.all().delete()

        return redirect("checkout:success", order_id=order.pk)


@login_req
class CheckoutSuccessView(TemplateView):
    """
    GET → after a successful payment, show a Thank‑You page.
    """
    template_name = "checkout/success.html"

    def get(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id, user=request.user)
        return render(request, self.template_name, {"order": order})


@login_req
class OrderHistoryView(ListView):
    """
    GET → paginated list of a user’s past orders.
    """
    model               = Order
    template_name       = "checkout/order_list.html"
    context_object_name = "orders"
    paginate_by         = 10

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-date")


# re‐export your webhook handler so core/urls.py can point at it
stripe_webhook = stripe_webhook
