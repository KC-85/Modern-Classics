from importlib import import_module
from django.test import SimpleTestCase


class UsersAppConfigTests(SimpleTestCase):
    def test_app_config_is_present(self):
        """
        Accept either 'apps.users' or 'users' package layouts.
        """
        mod = import_module("apps.users.apps")
        cfg = getattr(mod, "UsersConfig", None)
        self.assertIsNotNone(cfg, "UsersConfig not found in apps.users.apps")
        self.assertTrue(
            cfg.name.endswith(".users") or cfg.name == "users",
            f"Unexpected app name: {cfg.name}",
        )
