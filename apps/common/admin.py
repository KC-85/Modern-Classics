from django.contrib import admin
from .models import Newsletter, Contact, FAQ

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
    readonly_fields = ("subscribed_at",)
    search_fields = ("email",)

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
