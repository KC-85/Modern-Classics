import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

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
            total_amount=cart.total_amount,
            status="pending",
        )
        # move cart items → order items here if you have OrderItem model…
        cart.items.all().delete()
        return redirect("orders:checkout", order_id=order.pk)


@login_req
class OrderListView(ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"
    paginate_by = 10

    def get_queryset(self):
        # show only the current user’s orders, most recent first
        return (
            Order.objects
            .filter(user=self.request.user)
            .order_by("-created_at")
        )


@login_req
class OrderDetailView(DetailView):
    model = Order
    template_name = "orders/order_detail.html"
    context_object_name = "order"
    pk_url_kwarg = "pk"

    def get_queryset(self):
        # ensure a user can only view their own orders
        return Order.objects.filter(user=self.request.user)


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
            # This bit will attach your order.pk to the PaymentIntent
            payment_intent_data={
                "metadata": {
                    "order_id": order.pk,
                }
            },
            success_url=request.build_absolute_uri(reverse("orders:success", args=[order.pk])),
            cancel_url= request.build_absolute_uri(reverse("orders:cancel", args=[order.pk])),
        )

        # Save the Stripe PaymentIntent ID so the webhook can find this order
        order.stripe_intent_id = session.payment_intent
        order.save(update_fields=["stripe_intent_id"])

        return redirect(session.url, code=303)


@login_req
class SuccessView(TemplateView):
    template_name = "orders/success.html"

    def get(self, request, *args, **kwargs):
        # 1) load the order (URL is success/<int:pk>/)
        order = get_object_or_404(
            Order, pk=kwargs["pk"], user=request.user
        )

        # 2) send confirmation email
        send_mail(
            subject=f"[Modern Classics] Order #{order.id} Confirmed",
            message=(
                f"Hi {request.user.username},\n\n"
                f"Thank you for your purchase! "
                f"Your order #{order.id} for £{order.total_amount:.2f} "
                "has been received and is now being processed.\n\n"
                "We’ll let you know as soon as it ships.\n\n"
                "— Modern Classics"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[request.user.email],
            fail_silently=False,
        )

        # 3) render the page passing 'order' into context
        return self.render_to_response({"order": order})


@login_req
class CancelView(TemplateView):
    """
    GET → show an “Order canceled” page.
    """
    template_name = "orders/cancel.html"
