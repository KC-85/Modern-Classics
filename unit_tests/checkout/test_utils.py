from decimal import Decimal
from django.test import SimpleTestCase, override_settings
from apps.checkout.utils import compute_delivery


class ComputeDeliveryTests(SimpleTestCase):
    @override_settings(FREE_DELIVERY_THRESHOLD=Decimal("50.00"), STANDARD_DELIVERY_PERCENT=Decimal("10.0"))
    def test_below_threshold(self):
        self.assertEqual(compute_delivery(Decimal("40.00")), Decimal("4.00"))

    @override_settings(FREE_DELIVERY_THRESHOLD=Decimal("50.00"), STANDARD_DELIVERY_PERCENT=Decimal("10.0"))
    def test_at_threshold_free(self):
        self.assertEqual(compute_delivery(Decimal("50.00")), Decimal("0.00"))

    @override_settings(FREE_DELIVERY_THRESHOLD=Decimal("50.00"), STANDARD_DELIVERY_PERCENT=Decimal("7.5"))
    def test_custom_percent(self):
        self.assertEqual(compute_delivery(Decimal("20.00")), Decimal("1.50"))
