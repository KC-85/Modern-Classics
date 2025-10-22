from decimal import Decimal
from unittest.mock import patch, Mock
from django.test import TestCase, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model

from apps.checkout.models import Order, OrderLineItem
from apps.showroom.models import CarMake, CarModel, Car

User = get_user_model()

DUMMY_KEYS = dict(
    STRIPE_SECRET_KEY="sk_test_x",
    STRIPE_PUBLISHABLE_KEY="pk_test_x",
    STRIPE_WEBHOOK_SECRET="whsec_x",
)


@override_settings(**DUMMY_KEYS)
class CheckoutViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="u", password="x", email="u@example.com")
        make = CarMake.objects.create(name="Ford")
        model = CarModel.objects.create(make=make, name="Focus")
        cls.car = Car.objects.create(
            make=make, model=model, year=2020,
            specifications="Spec", performance="Perf",
            condition="good", price=Decimal("10000.00")
        )

    def setUp(self):
        self.client.force_login(self.user)

    @patch("apps.checkout.views.get_object_or_404")
    def test_create_order_view_builds_order_from_cart(self, mock_get):
        # Fake Cart and items
        cart = Mock()
        item = Mock()
        item.car = self.car
        item.car_id = self.car.id
        item.quantity = 2
        cart.items.exists.return_value = True
        cart.items.select_related.return_value = [item]
        mock_get.return_value = cart

        url = reverse("checkout:create_order")
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 302)
        # redirected to checkout page with created order id in URL
        self.assertIn(reverse("checkout:checkout", kwargs={
                      "order_id": 1})[:-2], resp.url)

        order = Order.objects.first()
        self.assertIsNotNone(order)
        self.assertEqual(order.user, self.user)
        self.assertEqual(order.lineitems.count(), 1)
        li = order.lineitems.first()
        self.assertEqual(li.quantity, 2)
        self.assertEqual(li.unit_price, Decimal("10000.00"))

    @patch("apps.checkout.views.stripe.PaymentIntent.create")
    @patch("apps.checkout.views.get_object_or_404")
    def test_checkout_view_get_sets_totals_and_creates_pi(self, mock_get, mock_pi_create):
        # Prepare order with one line item
        order = Order.objects.create(
            user=self.user, original_trailer={"items": []})
        OrderLineItem.objects.create(
            order=order, car=self.car, quantity=1, unit_price=self.car.price)
        # mock cart lookup inside CreateOrderView isn't used here; we mock get() to return order
        mock_get.return_value = order

        mock_pi_create.return_value = Mock(
            id="pi_123", client_secret="secret_123")

        url = reverse("checkout:checkout", kwargs={"order_id": order.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        order.refresh_from_db()
        # order_total equals item total
        self.assertEqual(order.order_total, Decimal("10000.00"))
        # delivery computed based on settings threshold (defaults → likely 0 if >=50)
        self.assertIsNotNone(order.delivery_cost)
        self.assertTrue(order.grand_total >= order.order_total)
        self.assertEqual(order.stripe_pid, "pi_123")
        mock_pi_create.assert_called_once()

    @patch("apps.checkout.views.send_mail")
    @patch("apps.checkout.views.Cart")
    def test_success_view_sends_receipt_and_marks_cars_sold_and_deletes_cart(self, mock_cart, mock_send):
        order = Order.objects.create(user=self.user, original_trailer={
                                     "items": []}, email="u@example.com")
        OrderLineItem.objects.create(
            order=order, car=self.car, quantity=1, unit_price=self.car.price)

        # Simulate a cart existing for this user
        mock_cart.objects.filter.return_value.first.return_value = Mock()

        url = reverse("checkout:success", kwargs={"order_id": order.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        # email sent
        self.assertTrue(mock_send.called)
        # car marked sold
        self.car.refresh_from_db()
        self.assertTrue(self.car.is_sold)
        # cart delete called
        self.assertTrue(
            mock_cart.objects.filter.return_value.first.return_value.delete.called)

    def test_order_detail_and_history_require_login_and_scope_to_user(self):
        # two users, two orders
        other = User.objects.create_user(
            username="o", password="x", email="o@example.com")
        my_order = Order.objects.create(
            user=self.user, original_trailer={"items": []})
        other_order = Order.objects.create(
            user=other, original_trailer={"items": []})

        # Order detail: I can see mine
        url = reverse("checkout:order_detail", kwargs={
                      "order_number": my_order.order_number})
        self.client.force_login(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        # I cannot see other's (404)
        url2 = reverse("checkout:order_detail", kwargs={
                       "order_number": other_order.order_number})
        resp2 = self.client.get(url2)
        self.assertEqual(resp2.status_code, 404)

        # Order history list scoped
        url3 = reverse("checkout:list")
        resp3 = self.client.get(url3)
        self.assertEqual(resp3.status_code, 200)
        self.assertQuerySetEqual(
            resp3.context["orders"], [my_order], transform=lambda o: o, ordered=False
        )
