import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
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
    GET → render checkout page with Stripe Elements
    POST → confirm the payment intent & then redirect to success
    """
    template_name = "orders/checkout/checkout.html"

    def get(self, request, order_id, *args, **kwargs):
        # 1) load the order
        order = get_object_or_404(Order, pk=order_id, user=request.user)

        # 2) create a PaymentIntent
        intent = stripe.PaymentIntent.create(
            amount=int(order.total_amount * 100),
            currency="gbp",
            metadata={"order_id": order.pk},
        )

        # 3) render the template with client_secret + public key
        return render(request, self.template_name, {
            "order": order,
            "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
            "client_secret": intent.client_secret,
        })

    def post(self, request, order_id, *args, **kwargs):
        # after stripe confirms card payment via JS, the form does a POST here
        order = get_object_or_404(Order, pk=order_id, user=request.user)

        # mark paid, send email, etc. (you can refactor this into SuccessView)
        order.status      = Order.Status.PAID
        order.paid_amount = order.total_amount
        order.currency    = "GBP"
        order.save(update_fields=["status","paid_amount","currency"])

        # now email user
        subject = f"Your Order #{order.pk} Confirmation"
        message = (
            f"Hi {order.user.username},\n\n"
            f"Thanks for your purchase! Order #{order.pk} is now paid.\n"
            f"Total paid: £{order.total_amount:.2f}\n\n"
            f"View details: {request.build_absolute_uri(reverse('orders:detail', args=[order.pk]))}\n"
        )
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [order.user.email])

        return redirect("orders:success", order_id=order.pk)


@login_req
class SuccessView(TemplateView):
    template_name = "orders/success.html"

    def get(self, request, order_id, *args, **kwargs):
        # 1) Fetch & mark paid
        order = get_object_or_404(Order, pk=order_id, user=request.user)
        if order.status == Order.Status.PENDING:
            order.status      = Order.Status.PAID
            order.paid_amount = order.total_amount
            order.currency    = "GBP"
            order.save(update_fields=["status", "paid_amount", "currency"])

            # 2) Send confirmation email
            subject = f"Your Order #{order.pk} Confirmation"
            message = (
                f"Hi {order.user.username},\n\n"
                f"Thank you for your purchase! Your order #{order.pk} has been received and marked as paid.\n\n"
                f"Order total: £{order.total_amount:.2f}\n"
                f"You can view your order here: {request.build_absolute_uri(reverse('orders:detail', args=[order.pk]))}\n\n"
                "We’ll be in touch with delivery details shortly.\n\n"
                "Best,\n"
                "The Classics Team"
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [order.user.email]

            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
            )

        # 3) Render the success page
        return render(request, self.template_name, {"order": order})


@login_req
class CancelView(TemplateView):
    """
    GET → show an “Order canceled” page.
    """
    template_name = "orders/cancel.html"
