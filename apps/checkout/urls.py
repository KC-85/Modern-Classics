from django.urls import path
from .views import (
    cache_checkout_data, 
    CheckoutView,
    CheckoutSuccessView, 
    stripe_webhook,
    order_history
)

app_name = "checkout"

urlpatterns = [
    path('history/', order_history, name='order_history'),
    path("cache-data/", cache_checkout_data, name="cache_data"),
    path("<int:order_id>/", CheckoutView.as_view(), name="checkout"),
    path("success/<int:order_id>/", CheckoutSuccessView.as_view(), name="success"),
    path("stripe/webhook/", stripe_webhook, name="stripe-webhook"),
]
