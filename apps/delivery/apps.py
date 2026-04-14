"""Application configuration for the delivery app.

Defines AppConfig metadata used by Django during startup and app registry loading."""

from django.apps import AppConfig

class DeliveryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.delivery"
    verbose_name = "Delivery"
