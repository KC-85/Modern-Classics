from django.contrib import admin
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase


class UsersAdminRegistrationTests(SimpleTestCase):
    def test_user_model_is_registered(self):
        """
        Your custom user model should be visible in the admin site registry.
        """
        User = get_user_model()
        self.assertIn(
            User, admin.site._registry,
            f"{User.__name__} is not registered in admin.site",
        )
