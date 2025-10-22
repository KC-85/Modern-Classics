from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model

from apps.checkout.models import Order, OrderLineItem
from apps.showroom.models import CarMake, CarModel, Car

User = get_user_model()


class CheckoutModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="buyer", password="x", email="buyer@example.com")
        make = CarMake.objects.create(name="Ford")
        model = CarModel.objects.create(make=make, name="Focus")
        cls.car = Car.objects.create(
            make=make, model=model, year=2020,
            specifications="Spec", performance="Perf",
            condition="good", price=Decimal("12345.67")
        )

    def test_lineitem_total_and_order_totals(self):
        order = Order.objects.create(
            user=self.user,
            original_trailer={"items": []},
        )
        li = OrderLineItem.objects.create(
            order=order, car=self.car, quantity=2, unit_price=Decimal("100.00")
        )
        self.assertEqual(li.lineitem_total, Decimal("200.00"))

        order.refresh_from_db()
        # save() recomputes totals
        order.save()
        self.assertEqual(order.order_total, Decimal("200.00"))
        self.assertEqual(order.grand_total, Decimal("200.00"))

        # add delivery cost and ensure grand_total updates
        order.delivery_cost = Decimal("5.00")
        order.save(update_fields=["delivery_cost"])
        order.save()
        self.assertEqual(order.grand_total, Decimal("205.00"))

    def test_is_paid_property(self):
        order = Order.objects.create(
            user=self.user, original_trailer={"items": []})
        self.assertFalse(order.is_paid)
        order.status = Order.PaymentStatus.PAID
        order.save(update_fields=["status"])
        self.assertTrue(order.is_paid)
