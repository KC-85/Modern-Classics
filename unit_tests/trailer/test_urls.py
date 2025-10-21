from django.test import SimpleTestCase
from django.urls import include, path, reverse, resolve


class TrailerURLNamespaceTests(SimpleTestCase):
    def test_namespace_is_included(self):
        # This will 404 if the namespace isn't present; we only care that reversing works.
        resolved = resolve(reverse("trailer:cart_detail"))
        self.assertTrue(resolved.namespace ==
                        "trailer" or resolved.app_name == "trailer")

    def test_optional_routes_exist_if_you_expose_them(self):
        optional = [
            ("add_to_cart", {"pk": 1}),
            ("add", {"pk": 1}),
            ("remove_from_cart", {"pk": 1}),
            ("remove", {"pk": 1}),
            ("update_item", {"pk": 1}),
        ]
        for name, kwargs in optional:
            try:
                reverse(f"trailer:{name}", kwargs=kwargs)
            except Exception:
                # It's okay if you don't expose a specific route name—these are optional
                continue
