from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory, override_settings
from django.utils import timezone

from apps.checkout.models import Order
from apps.checkout.webhook_handler import StripeWH_Handler

User = get_user_model()


@override_settings(DEFAULT_FROM_EMAIL="noreply@example.com")
class StripeWebhookHandlerTests(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.user = User.objects.create_user(
			username="wh-user", password="pass", email="buyer@example.com"
		)

	def _create_order(self):
		return Order.objects.create(
			user=self.user,
			full_name="Buyer Name",
			email="buyer@example.com",
			phone_number="01234567890",
			country="GB",
			postcode="SW1A 1AA",
			town_or_city="London",
			street_address1="10 Downing Street",
			street_address2="",
			county="Greater London",
			original_trailer={"items": []},
		)

	def test_payment_intent_succeeded_marks_order_paid(self):
		order = self._create_order()
		request = self.factory.post("/checkout/webhook/", data=b"{}", content_type="application/json")
		handler = StripeWH_Handler(request)

		event = {
			"type": "payment_intent.succeeded",
			"data": {
				"object": {
					"id": "pi_123",
					"metadata": {"order_id": str(order.pk)},
					"amount_received": 1050000,
					"currency": "gbp",
				}
			},
		}

		response = handler.handle_payment_intent_succeeded(event)

		self.assertEqual(response.status_code, 200)
		order.refresh_from_db()
		self.assertEqual(order.status, Order.PaymentStatus.PAID)
		self.assertEqual(order.paid_amount, Decimal("10500.00"))
		self.assertEqual(order.currency, "GBP")
		self.assertEqual(order.stripe_pid, "pi_123")
		self.assertIsNotNone(order.paid_at)

	def test_payment_intent_succeeded_is_idempotent_for_already_paid_order(self):
		order = self._create_order()
		original_paid_at = timezone.now()
		order.status = Order.PaymentStatus.PAID
		order.paid_at = original_paid_at
		order.paid_amount = Decimal("9999.99")
		order.currency = "GBP"
		order.stripe_pid = "pi_existing"
		order.save(update_fields=["status", "paid_at", "paid_amount", "currency", "stripe_pid"])

		request = self.factory.post("/checkout/webhook/", data=b"{}", content_type="application/json")
		handler = StripeWH_Handler(request)

		event = {
			"type": "payment_intent.succeeded",
			"data": {
				"object": {
					"id": "pi_retry",
					"metadata": {"order_id": str(order.pk)},
					"amount_received": 105000,
					"currency": "gbp",
				}
			},
		}

		response = handler.handle_payment_intent_succeeded(event)

		self.assertEqual(response.status_code, 200)
		order.refresh_from_db()
		self.assertEqual(order.status, Order.PaymentStatus.PAID)
		self.assertEqual(order.paid_amount, Decimal("9999.99"))
		self.assertEqual(order.currency, "GBP")
		self.assertEqual(order.stripe_pid, "pi_existing")
		self.assertEqual(order.paid_at, original_paid_at)

	def test_payment_intent_failed_marks_order_failed(self):
		order = self._create_order()
		request = self.factory.post("/checkout/webhook/", data=b"{}", content_type="application/json")
		handler = StripeWH_Handler(request)

		event = {
			"type": "payment_intent.payment_failed",
			"data": {
				"object": {
					"metadata": {"order_id": str(order.pk)},
				}
			},
		}

		response = handler.handle_payment_intent_payment_failed(event)

		self.assertEqual(response.status_code, 200)
		order.refresh_from_db()
		self.assertEqual(order.status, Order.PaymentStatus.FAILED)
