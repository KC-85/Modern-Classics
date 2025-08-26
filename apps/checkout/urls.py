from django.urls import path
from .views import (
    cache_checkout_data,
    CreateOrderView, 
    CheckoutView,
    CheckoutSuccessView, 
    stripe_webhook,
    OrderHistoryView,
)

app_name = "checkout"

urlpatterns = [
    path("cache-data/", cache_checkout_data, name="cache_data"),
    path("order/create/", CreateOrderView.as_view(), name="create_order"),
    path("<int:order_id>/", CheckoutView.as_view(), name="checkout"),
    path("success/<int:order_id>/", CheckoutSuccessView.as_view(), name="success"),
    path("stripe/webhook/", stripe_webhook, name="stripe-webhook"),
    path('list/', OrderHistoryView.as_view(), name='list'),
]
