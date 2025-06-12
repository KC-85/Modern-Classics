from django.contrib import admin
from .models import DeliveryOption, OrderDelivery

@admin.register(DeliveryOption)
class DeliveryOptionAdmin(admin.ModelAdmin):
    list_display   = ("name", "fee")
    search_fields  = ("name",)
    list_editable  = ("fee",)

@admin.register(OrderDelivery)
class OrderDeliveryAdmin(admin.ModelAdmin):
    list_display   = ("order", "option", "tracking_id", "shipped_at")
    list_filter    = ("option", "shipped_at")
    search_fields  = ("order__id", "tracking_id")
    raw_id_fields  = ("order",)
