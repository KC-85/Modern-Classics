from django.test import TestCase
from django.contrib import admin
from django.contrib.admin.sites import site

from apps.checkout.models import Order, OrderLineItem


class CheckoutAdminTests(TestCase):
    def test_admin_registered(self):
        self.assertIsInstance(site._registry.get(Order), admin.ModelAdmin)

    def test_order_admin_config(self):
        ma = site._registry[Order]
        # inlines
        self.assertTrue(any(i.model is OrderLineItem for i in ma.inlines))
        # readonly fields
        for f in (
            "order_number", "date", "order_total", "delivery_cost", "grand_total",
            "original_trailer", "stripe_pid", "paid_amount", "currency", "paid_at"
        ):
            self.assertIn(f, ma.readonly_fields)
        # list display basics
        for f in ("order_number", "status", "grand_total", "date"):
            self.assertIn(f, ma.list_display)
