# apps/orders/urls.py
from django.urls import path
from .views import (
    CreateOrderView, CheckoutView,
    SuccessView, CancelView
)

app_name = "orders"

urlpatterns = [
    path("create/",                  CreateOrderView.as_view(), name="create_order"),
    path("checkout/<int:order_id>/", CheckoutView.as_view(),     name="checkout"),
    path("success/",                 SuccessView.as_view(),      name="success"),
    path("cancel/",                  CancelView.as_view(),       name="cancel"),
]
