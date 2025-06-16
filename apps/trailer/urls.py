# apps/trailer/urls.py
from django.urls import path
from .views import (
    CartDetailView, AddToCartView,
    UpdateCartItemView, ClearCartView
)

app_name = "trailer"

urlpatterns = [
    path("",                       CartDetailView.as_view(),    name="cart_detail"),
    path("add/<int:car_pk>/",      AddToCartView.as_view(),     name="add_to_cart"),
    path("item/<int:item_pk>/edit/", UpdateCartItemView.as_view(), name="update_cart_item"),
    path("clear/",                 ClearCartView.as_view(),     name="clear_cart"),
]
