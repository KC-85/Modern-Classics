from decimal import Decimal
from unittest.mock import patch
from django.test import TestCase, override_settings, RequestFactory
from django.http import HttpResponse

from apps.checkout.webhook_handler import StripeWH_Handler
from apps.checkout.webhooks import stripe_webhook
from apps.checkout.models import Order


@override_settings(STRIPE_SECRET_KEY="sk_x", STRIPE_WEBHOOK_SECRET="whsec_x", DEFAULT_FROM_EMAIL="noreply@example.com")
class WebhookHandlerTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.order = Order.objects.create(
            user=None, original_trailer={"items": []})

    @patch("apps.checkout.webhook_handler.send_mail")
    def test_payment_intent_succeeded_updates_order(self, mock_send):
        self.order.email = "buyer@example.com"
        self.order.save(update_fields=["email"])
        handler = StripeWH_Handler(self.factory.post("/"))
        event = {
            "data": {
                "object": {
                    "id": "pi_123",
                    "amount_received": 12345,
                    "currency": "gbp",
                    "metadata": {"order_id": self.order.pk},
                }
            }
        }
        resp = handler.handle_payment_intent_succeeded(event)
        self.assertIsInstance(resp, HttpResponse)
        self.order.refresh_from_db()
        self.assertEqual(self.order.stripe_pid, "pi_123")
        self.assertEqual(self.order.paid_amount, Decimal("123.45"))
        self.assertEqual(self.order.currency, "GBP")
        self.assertEqual(self.order.status, Order.PaymentStatus.PAID)
        self.assertIsNotNone(self.order.paid_at)
        self.assertTrue(mock_send.called)

    def test_payment_intent_failed_marks_failed(self):
        handler = StripeWH_Handler(self.factory.post("/"))
        event = {
            "data": {"object": {"metadata": {"order_id": self.order.pk}}}
        }
        resp = handler.handle_payment_intent_payment_failed(event)
        self.assertIsInstance(resp, HttpResponse)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, Order.PaymentStatus.FAILED)

    def test_handle_event_fallback(self):
        handler = StripeWH_Handler(self.factory.post("/"))
        resp = handler.handle_event({"type": "unhandled.type"})
        self.assertEqual(resp.status_code, 200)

    @patch("apps.checkout.webhooks.StripeWH_Handler.handle_payment_intent_succeeded", return_value=HttpResponse(status=200))
    @patch("apps.checkout.webhooks.stripe.Webhook.construct_event", return_value={"type": "payment_intent.succeeded"})
    def test_webhook_dispatch_success(self, mock_construct, mock_handler):
        req = self.factory.post(
            "/stripe/webhook/", data=b"{}", content_type="application/json")
        resp = stripe_webhook(req)
        self.assertEqual(resp.status_code, 200)
        mock_construct.assert_called_once()
        mock_handler.assert_called_once()

    @patch("apps.checkout.webhooks.stripe.Webhook.construct_event", side_effect=ValueError)
    def test_webhook_bad_json(self, mock_construct):
        req = self.factory.post(
            "/stripe/webhook/", data=b"not-json", content_type="application/json")
        resp = stripe_webhook(req)
        self.assertEqual(resp.status_code, 400)

    @patch("apps.checkout.webhooks.stripe.Webhook.construct_event", side_effect=Exception)
    def test_webhook_unexpected_error(self, mock_construct):
        req = self.factory.post(
            "/stripe/webhook/", data=b"{}", content_type="application/json")
        resp = stripe_webhook(req)
        self.assertEqual(resp.status_code, 400)
