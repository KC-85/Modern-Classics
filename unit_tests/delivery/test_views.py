from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import get_resolver, reverse


User = get_user_model()


class DeliveryViewSmokeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="delivery-user", password="pass12345", email="user@example.com"
        )

    def test_all_delivery_urls_without_kwargs_are_reachable(self):
        """
        For every URL named `delivery:*` that does NOT require kwargs,
        hit it and accept 200/302/403 (login-required/admin-only pages).
        """
        resolver = get_resolver()
        names = [
            n for n, pat in resolver.reverse_dict.items()
            if isinstance(n, str) and n.startswith("delivery:")
        ]

        for name in names:
            # Only attempt reversing names with no kwargs pattern
            try:
                url = reverse(name)
            except Exception:
                continue  # needs kwargs; skip safely

            resp = self.client.get(url, follow=False)
            self.assertIn(
                resp.status_code,
                {200, 302, 403},
                msg=f"{name} returned {resp.status_code}"
            )

    def test_regular_user_cannot_access_delivery_option_management(self):
        self.client.force_login(self.user)

        for name in ["delivery:option_list", "delivery:option_add"]:
            resp = self.client.get(reverse(name))
            self.assertEqual(resp.status_code, 403, msg=f"{name} should be 403")

        from apps.delivery.models import DeliveryOption

        option = DeliveryOption.objects.create(
            name="Standard", price="10.00", description="Standard delivery"
        )

        for name in ["delivery:option_edit", "delivery:option_delete"]:
            resp = self.client.get(reverse(name, kwargs={"pk": option.pk}))
            self.assertEqual(resp.status_code, 403, msg=f"{name} should be 403")
