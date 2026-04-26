"""View logic for the trailer app.

Handles HTTP requests, orchestrates domain operations, and returns rendered responses."""

# apps/trailer/views.py
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from apps.common.auth_mixins import LoginRequiredMessageMixin  # <-- use your mixin
from .models import Cart, CartItem
from .forms  import AddToCartForm, UpdateCartForm


class CartDetailView(LoginRequiredMessageMixin, View):
    template_name = "trailer/cart_detail.html"

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        return render(request, self.template_name, {"cart": cart})


class AddToCartView(LoginRequiredMessageMixin, View):
    form_class = AddToCartForm

    def post(self, request, car_pk):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        form = self.form_class(request.POST)
        if form.is_valid():
            qty = form.cleaned_data["quantity"]
            item, created = CartItem.objects.get_or_create(
                cart=cart,
                car_id=car_pk,
                defaults={"quantity": qty},
            )
            if not created:
                item.quantity += qty
                item.save()
                messages.success(
                    request,
                    f"Updated quantity of {item.car} in your cart (now {item.quantity})."
                )
            else:
                messages.success(
                    request,
                    f"✓ Added {item.car} to your cart."
                )
        return redirect("trailer:cart_detail")


class UpdateCartItemView(LoginRequiredMessageMixin, View):
    form_class = UpdateCartForm

    def post(self, request, item_pk):
        item = get_object_or_404(
            CartItem,
            pk=item_pk,
            cart__user=request.user
        )
        try:
            qty = int(request.POST.get("quantity", 1))
        except ValueError:
            qty = 1

        car_name = str(item.car)
        if qty < 1:
            item.delete()
            messages.success(request, f"Removed {car_name} from your cart.")
        else:
            item.quantity = qty
            item.save()
            messages.success(request, f"Updated {car_name} quantity to {qty}.")

        return redirect("trailer:cart_detail")


class ClearCartView(LoginRequiredMessageMixin, View):
    def post(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        count = cart.items.count()
        cart.items.all().delete()
        if count > 0:
            messages.success(request, f"Cleared your cart ({count} item(s) removed).")
        return redirect("trailer:cart_detail")
