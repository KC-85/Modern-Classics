from django.test import SimpleTestCase
from django.urls import resolve, reverse
from apps.checkout import views


class CheckoutURLTests(SimpleTestCase):
    def test_named_urls(self):
        self.assertEqual(resolve(reverse("checkout:cache_data")
                                 ).func, views.cache_checkout_data)
        self.assertEqual(resolve(reverse("checkout:create_order")
                                 ).func.view_class, views.CreateOrderView)
        self.assertEqual(resolve(reverse("checkout:checkout", kwargs={
                         "order_id": 1})).func.view_class, views.CheckoutView)
        self.assertEqual(resolve(reverse("checkout:order_detail", kwargs={
                         "order_number": "00000000-0000-0000-0000-000000000000"})).func.view_class, views.OrderDetailView)
        self.assertEqual(resolve(reverse("checkout:success", kwargs={
                         "order_id": 1})).func.view_class, views.CheckoutSuccessView)
        self.assertEqual(resolve(reverse("checkout:list")
                                 ).func.view_class, views.OrderHistoryView)
