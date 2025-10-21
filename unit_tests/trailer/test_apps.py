from django.test import TestCase
from django.apps import apps


class TrailerAppConfigTests(TestCase):
    def test_app_config(self):
        # Accept either "apps.trailer" or "trailer" style paths
        cfg = apps.get_app_config("trailer")
        self.assertEqual(cfg.name.split(".")[-1], "trailer")
