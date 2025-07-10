import json
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from ..trailer.models import Cart
from .models import Order

# initialize Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY

# decorator helper for class-based views
default_login = login_required
login_req = method_decorator(default_login, name='dispatch')

@login_required
@require_POST
@csrf_exempt
def cache_checkout_data(request):
    """
    AJAX endpoint to attach metadata to the PaymentIntent before confirming payment.
    """
    data = json.loads(request.body)
    pid = data.get('client_secret', '').split('_secret')[0]
    order_id = data.get('order_id')
    save_info = data.get('save_info', False)

    stripe.PaymentIntent.modify(
        pid,
        metadata={
            'order_id': order_id,
            'save_info': save_info,
        }
    )
    return HttpResponse(status=200)

@login_req
class CreateOrderView(View):
    """
    POST → convert the current user's Cart into an Order,
    then redirect into the Elements-based checkout.
    """
    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        order = Order.objects.create(
            user=request.user,
            total_amount=cart.total_amount,
            status=Order.Status.PENDING,
        )
        # TODO: copy cart items into OrderItem if desired
        cart.items.all().delete()
        return redirect('orders:checkout', order_id=order.pk)

@login_req
class ElementsCheckoutView(View):
    """
    GET → create a PaymentIntent and render the Stripe Elements checkout form.
    POST → after JS confirms card, mark order as paid and redirect to success.
    """
    template_name = 'orders/checkout/checkout.html'

    def get(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id, user=request.user)
        cart  = Cart.objects.get(user=request.user)

        # Create PaymentIntent
        amount = int(order.total_amount * 100)
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='gbp',
            metadata={'order_id': order.pk},
        )

        context = {
            'client_secret':     intent.client_secret,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'order':             order,
            'bag_items':         cart.items.all(),
            'product_count':     cart.items.count(),
            'total':             order.total_amount,
            'delivery':          order.delivery_fee,
            'grand_total':       order.total_with_delivery,
        }
        return render(request, self.template_name, context)

    def post(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id, user=request.user)
        if order.status == Order.Status.PENDING:
            order.status      = Order.Status.PAID
            order.paid_amount = order.total_amount
            order.currency    = 'GBP'
            order.save(update_fields=['status', 'paid_amount', 'currency'])
        return redirect('orders:success', order_id=order.pk)

@login_req
class SuccessView(TemplateView):
    """
    GET → show a Thank You page; order is already marked paid.
    """
    template_name = 'orders/success.html'

    def get(self, request, order_id, *args, **kwargs):
        order = get_object_or_404(Order, pk=order_id, user=request.user)
        return render(request, self.template_name, {'order': order})

@login_req
class CancelView(TemplateView):
    """
    GET → show an Order Canceled page.
    """
    template_name = 'orders/cancel.html'

@login_req
class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_queryset(self):
        return (
            Order.objects
                 .filter(user=self.request.user)
                 .order_by('-created_at')
        )

@login_req
class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
