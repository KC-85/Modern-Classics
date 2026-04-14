"""Application configuration for the common app.

Defines AppConfig metadata used by Django during startup and app registry loading."""

# apps/common/apps.py

from django.apps import AppConfig

class CommonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.common"
    verbose_name = "Common Utilities"
