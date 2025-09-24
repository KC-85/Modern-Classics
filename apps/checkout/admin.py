# checkout/admin.py

from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    extra = 0
    fields = ("car", "quantity", "unit_price", "lineitem_total")
    readonly_fields = ("lineitem_total",)
    autocomplete_fields = ("car",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemInline,)

    # Make computed & system fields read-only
    readonly_fields = (
        "order_number",
        "date",
        "order_total",
        "delivery_cost",
        "grand_total",
        "original_trailer",
        "stripe_pid",
        "paid_amount",
        "currency",
        "paid_at",
    )

    # Field layout in the edit page
    fieldsets = (
        ("Order", {
            "fields": ("order_number", "user", "date", "status")
        }),
        ("Contact & Delivery Address", {
            "fields": (
                "full_name", "email", "phone_number",
                "street_address1", "street_address2",
                "town_or_city", "county", "postcode", "country",
            )
        }),
        ("Totals", {
            "fields": ("order_total", "delivery_cost", "grand_total")
        }),
        ("Payment", {
            "fields": ("stripe_pid", "paid_amount", "currency", "paid_at")
        }),
        ("Snapshot", {
            "classes": ("collapse",),
            "fields": ("original_trailer",),
        }),
    )

    # List page columns
    list_display = (
        "order_number",
        "user",
        "status",
        "grand_total",
        "paid_amount",
        "currency",
        "paid_at",
        "date",
    )
    list_filter = ("status", "date", "paid_at", "country")
    search_fields = ("order_number", "email", "full_name", "user__email")
    date_hierarchy = "date"
    ordering = ("-date",)

    list_select_related = ("user",)

    # Emphasize paid vs pending with row class
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related("lineitems", "lineitems__car")
