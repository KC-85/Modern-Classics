# unit_tests/common/test_apps.py
from django.apps import apps
from django.test import SimpleTestCase

from apps.common.apps import CommonConfig


class CommonAppsConfigTests(SimpleTestCase):
    def test_app_config_registered(self):
        """AppConfig should be discoverable via apps.get_app_config."""
        cfg = apps.get_app_config("common")
        self.assertIsNotNone(cfg)
        self.assertEqual(cfg.name, "apps.common")
        self.assertIsInstance(cfg, CommonConfig)

    def test_label_and_verbose_name(self):
        """Labels are stable; verbose_name optional unless you set it."""
        cfg = apps.get_app_config("common")
        self.assertEqual(cfg.label, "common")
        # Only assert verbose_name if you set one in CommonConfig; otherwise ensure it’s a str
        self.assertIsInstance(getattr(cfg, "verbose_name", "Common"), str)

    def test_ready_does_not_crash(self):
        """ready() should be safe to call multiple times."""
        cfg = apps.get_app_config("common")
        # If you connect signals in ready(), calling twice should still be safe (idempotent).
        cfg.ready()
        cfg.ready()  # no exception
