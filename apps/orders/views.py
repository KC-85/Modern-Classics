import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView

from ..trailer.models import Cart
from .models import Order

# initialize Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# decorator helper
login_req = method_decorator(login_required, name="dispatch")


@login_req
class CreateOrderView(View):
    """
    POST → convert the current user's Cart into an Order,
    clear the cart, then redirect to Stripe checkout.
    """
    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        order = Order.objects.create(
            user=request.user,
            total_amount=cart.get_total(),  # you’ll need a get_total() helper
            status="pending",
        )
        # move cart items → order items here if you have OrderItem model…
        cart.items.all().delete()
        return redirect("orders:checkout", order_id=order.pk)


@login_req
class CheckoutView(View):
    """
    GET → create a Stripe Checkout Session for the Order
    and redirect the user into Stripe’s hosted payment page.
    """
    def get(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id, user=request.user)
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "gbp",
                    "unit_amount": int(order.total_amount * 100),
                    "product_data": {"name": f"Order #{order.pk}"},
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url=request.build_absolute_uri(reverse("orders:success")),
            cancel_url= request.build_absolute_uri(reverse("orders:cancel")),
        )
        return redirect(session.url, code=303)


@login_req
class SuccessView(TemplateView):
    """
    GET → show a “Thank you for your order” page.
    """
    template_name = "orders/success.html"


@login_req
class CancelView(TemplateView):
    """
    GET → show an “Order canceled” page.
    """
    template_name = "orders/cancel.html"
