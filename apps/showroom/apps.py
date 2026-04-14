"""Application configuration for the showroom app.

Defines AppConfig metadata used by Django during startup and app registry loading."""

# apps/showroom/apps.py

from django.apps import AppConfig

class ShowroomConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.showroom"
    verbose_name = "Car Showroom"
