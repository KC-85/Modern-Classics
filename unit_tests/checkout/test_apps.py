from django.test import SimpleTestCase
from django.apps import apps


class CheckoutAppConfigTests(SimpleTestCase):
    def test_config_present(self):
        cfg = apps.get_app_config("checkout")
        self.assertEqual(cfg.name, "apps.checkout")
