from django.test import TestCase
from django.urls import get_resolver, reverse


class DeliveryViewSmokeTests(TestCase):
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
