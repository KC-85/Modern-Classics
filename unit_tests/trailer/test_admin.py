from django.contrib import admin
from django.test import TestCase

from apps.trailer.models import Cart, CartItem


class TrailerAdminRegistrationTests(TestCase):
    def test_cart_registered(self):
        self.assertIn(
            Cart, admin.site._registry, "Cart is not registered in admin.site"
        )

    def test_cartitem_registered(self):
        self.assertIn(
            CartItem, admin.site._registry, "CartItem is not registered in admin.site"
        )
