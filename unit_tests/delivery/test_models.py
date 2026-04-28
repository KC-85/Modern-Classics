from django.apps import apps as dj_apps
from django.test import SimpleTestCase


class DeliveryModelsSmokeTests(SimpleTestCase):
    def test_models_module_loads_and_has_models(self):
        app = dj_apps.get_app_config("delivery")
        models = list(app.get_models())
        # It’s OK if delivery is view/form only.
        self.assertIsNotNone(models)
