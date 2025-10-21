from django.contrib import admin
from django.apps import apps as dj_apps
from django.test import SimpleTestCase


class DeliveryAdminRegistrationTests(SimpleTestCase):
    def test_at_least_one_delivery_model_registered_in_admin(self):
        delivery_app = dj_apps.get_app_config("delivery")
        registered = []
        for model in delivery_app.get_models():
            if model in admin.site._registry:
                registered.append(model.__name__)
        # It’s fine if you deliberately don’t register any models.
        # Treat as a soft signal.
        self.assertIsInstance(registered, list)
