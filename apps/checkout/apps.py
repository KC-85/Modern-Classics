"""Application configuration for the checkout app.

Defines AppConfig metadata used by Django during startup and app registry loading."""

# checkout/apps.py
from django.apps import AppConfig

class CheckoutConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.checkout"
