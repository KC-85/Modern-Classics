"""Django admin configuration for the common app.

Registers models and customizes list displays, filters, and management actions."""

from django.contrib import admin
from django.utils.html import format_html
from .models import Newsletter, Contact, FAQ, NewsletterEmail

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    readonly_fields = ("subscribed_at",)
    search_fields = ("email",)


@admin.register(NewsletterEmail)
class NewsletterEmailAdmin(admin.ModelAdmin):
    list_display = ("subject", "status_badge", "recipient_count", "created_at", "sent_at")
    list_filter = ("status", "created_at", "sent_at")
    search_fields = ("subject",)
    readonly_fields = ("sent_at", "recipient_count", "created_at")
    fields = ("subject", "body", "status", "scheduled_at", "created_at", "sent_at", "recipient_count")

    def status_badge(self, obj):
        """Display status as a colored badge."""
        colors = {
            "draft": "#FFC107",
            "scheduled": "#17A2B8",
            "sent": "#28A745",
        }
        color = colors.get(obj.status, "#6C757D")
        return format_html(
            '<span style="background-color: {}; color: white; padding: 5px 10px; border-radius: 3px;">{}</span>',
            color,
            obj.get_status_display(),
        )
    status_badge.short_description = "Status"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "date_sent", "is_resolved")
    list_filter  = ("is_resolved", "date_sent")
    search_fields = ("name", "email", "message")
    readonly_fields = ("date_sent",)
    actions = ["mark_resolved"]

    def mark_resolved(self, request, queryset):
        queryset.update(is_resolved=True)
    mark_resolved.short_description = "Mark selected contacts as resolved"


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "order")
    list_editable = ("order",)
    ordering = ("order",)
    search_fields = ("question", "answer")
