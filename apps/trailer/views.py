from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from .models import Cart, CartItem
from .forms import AddToCartForm, UpdateCartForm

"""
These are the views for the trailer (Cart),
these also require the user to be logged in to their own account
via login method decorators.
"""

# Cart detail view
@method_decorator(login_required, name="dispatch")
class CartDetailView(View):
    template_name = "trailer/cart_detail.html"

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        return render(request, self.template_name, {"cart": cart})

# Add to cart view
@method_decorator(login_required, name="dispatch")
class AddToCartView(View):
    form_class = AddToCartForm

    def post(self, request, car_pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            cart, _ = Cart.objects.get_or_create(user=request.user)
            item, created = CartItem.objects.get_or_create(
                cart=cart,
                car_id=car_pk,
                defaults={"quantity": form.cleaned_data["quantity"]},
            )
            if not created:
                item.quantity += form.cleaned_data["quantity"]
                item.save()
        return redirect("trailer:cart_detail")

# Update cart view
@method_decorator(login_required, name="dispatch")
class UpdateCartItemView(View):
    form_class = UpdateCartForm

    def post(self, request, item_pk):
        item = get_object_or_404(CartItem, pk=item_pk, cart__user=request.user)
        form = self.form_class(request.POST)
        if form.is_valid():
            item.quantity = form.cleaned_data["quantity"]
            item.save()
        return redirect("trailer:cart_detail")

# Clear cart view
@method_decorator(login_required, name="dispatch")
class ClearCartView(View):
    def post(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart.items.all().delete()
        return redirect("trailer:cart_detail")
