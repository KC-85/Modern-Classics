# apps/trailer/views.py
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

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

        if qty < 1:
            item.delete()
        else:
            item.quantity = qty
            item.save()

        return redirect("trailer:cart_detail")


class ClearCartView(LoginRequiredMessageMixin, View):
    def post(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart.items.all().delete()
        return redirect("trailer:cart_detail")
