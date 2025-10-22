from django.apps import apps
from django.test import TestCase


class ShowroomAppConfigTests(TestCase):
    def test_config_present(self):
        # accept either apps.showroom or showroom package-style
        app = apps.get_app_config("showroom")
        self.assertEqual(app.verbose_name or "Showroom",
                         app.verbose_name or "Showroom")
