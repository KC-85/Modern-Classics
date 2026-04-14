"""Application configuration for the trailer app.

Defines AppConfig metadata used by Django during startup and app registry loading."""

from django.apps import AppConfig

class TrailerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.trailer"
    verbose_name = "Trailer (Shopping Cart)"
