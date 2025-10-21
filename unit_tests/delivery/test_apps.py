from django.test import SimpleTestCase
from importlib import import_module


class DeliveryAppConfigTests(SimpleTestCase):
    def test_app_config_name_is_delivery(self):
        """
        Accept either `apps.delivery` or `delivery` depending on your layout.
        """
        mod = import_module("apps.delivery.apps")
        cfg = getattr(mod, "DeliveryConfig", None)
        self.assertIsNotNone(
            cfg, "DeliveryConfig not found in apps.delivery.apps")
        name = cfg.name
        self.assertTrue(name.endswith(".delivery") or name == "delivery")
