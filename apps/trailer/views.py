from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from .models import Cart, CartItem
from .forms  import AddToCartForm, UpdateCartForm

@method_decorator(login_required, name="dispatch")
class CartDetailView(View):
    template_name = "trailer/cart_detail.html"

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        return render(request, self.template_name, {"cart": cart})


@method_decorator(login_required, name="dispatch")
class AddToCartView(View):
    form_class = AddToCartForm

    def post(self, request, car_pk):
        # car_pk comes from your URL pattern
        cart, _ = Cart.objects.get_or_create(user=request.user)
        form = self.form_class(request.POST)
        if form.is_valid():
            qty = form.cleaned_data["quantity"]
            # Using get_or_create on CartItem by car_id
            item, created = CartItem.objects.get_or_create(
                cart=cart,
                car_id=car_pk,
                defaults={"quantity": qty},
            )
            if not created:
                item.quantity += qty
                item.save()
        return redirect("trailer:cart_detail")


@method_decorator(login_required, name="dispatch")
class UpdateCartItemView(View):
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


@method_decorator(login_required, name="dispatch")
class ClearCartView(View):
    def post(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart.items.all().delete()
        return redirect("trailer:cart_detail")
