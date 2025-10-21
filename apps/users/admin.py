# apps/users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # What shows up in the changelist
    list_display = (
        "username", "email", "first_name", "last_name",
        "is_staff", "is_active",
    )
    list_filter = ("is_staff", "is_active", "is_superuser", "date_joined")
    search_fields = ("username", "email", "first_name",
                     "last_name", "phone_number")
    ordering = ("-date_joined",)

    # Edit form layout
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {
            "fields": (
                "first_name", "last_name", "email",
                "phone_number", "date_of_birth", "profile_image",
            )
        }),
        ("Address", {
            "fields": (
                "address_line1", "address_line2",
                "city", "postal_code", "country",
            )
        }),
        ("Permissions", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Add form layout
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "is_staff", "is_active"),
        }),
    )
