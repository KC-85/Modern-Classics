from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, NoReverseMatch

User = get_user_model()


class UsersViewsSmokeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="viewer",
            email="viewer@example.com",
            password="pass1234",
        )

    def _reverse_or_none(self, name):
        try:
            return reverse(name)
        except NoReverseMatch:
            return None

    def test_profile_page_reachable_when_defined(self):
        url = self._reverse_or_none("users:profile")
        if not url:
            self.skipTest(
                "Enable after you expose a profile view under users:")
        # ✅ Avoid django-axes backend: bypass auth backends entirely
        self.client.force_login(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_orders_page_if_present(self):
        # Accept either namespace you might have used
        url = self._reverse_or_none(
            "users:orders") or self._reverse_or_none("orders:my_orders")
        if not url:
            self.skipTest("No orders page exposed under users: or orders:")
        self.client.login(username="viewer", password="pass1234")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
