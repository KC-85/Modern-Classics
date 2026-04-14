"""Application configuration for the users app.

Defines AppConfig metadata used by Django during startup and app registry loading."""

# apps/users/apps.py

from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"
    verbose_name = "User Management"
