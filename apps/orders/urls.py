# apps/orders/urls.py
from django.urls import path
from .webhooks import stripe_webhook
from .views import (
    CreateOrderView, OrderListView, OrderDetailView, 
    CheckoutView, SuccessView, CancelView
)

app_name = "orders"

urlpatterns = [
    # Create a new order from the cart
    path("create/", CreateOrderView.as_view(), name="create_order"),

    # Launch Stripe Checkout for a given order
    path("checkout/<int:order_id>/", CheckoutView.as_view(), name="checkout"),

    # Success redirect (marks order paid)
    path("success/<int:order_id>/", SuccessView.as_view(), name="success"),

    # Cancel redirect
    path("cancel/<int:order_id>/", CancelView.as_view(), name="cancel"),

    # Stripe webhook endpoint
    path("stripe/webhook/", stripe_webhook, name="stripe-webhook"),

    # List & detail views for the user’s orders
    path("", OrderListView.as_view(), name="list"),
    path("<int:pk>/", OrderDetailView.as_view(), name="detail"),
]
