# unit_tests/common/test_admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.common.models import Newsletter
from apps.common.admin import NewsletterAdmin  # ensures import doesn’t break

User = get_user_model()


class NewsletterAdminTests(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            email="admin@example.com",
            password="pass1234",
            username="admin",  # in case username is still required by your User model
        )
        self.client.force_login(self.superuser)

    def test_model_is_registered_with_admin(self):
        """Newsletter must be registered in the admin site."""
        self.assertIn(Newsletter, admin.site._registry)
        self.assertIsInstance(
            admin.site._registry[Newsletter], NewsletterAdmin)

    def test_admin_changelist_loads(self):
        """Superuser can load the changelist page."""
        url = reverse("admin:common_newsletter_changelist")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        # basic smoke content
        self.assertContains(resp, "Newsletter")

    def test_admin_add_form_creates_newsletter(self):
        """Posting the admin add form should create a record and redirect."""
        add_url = reverse("admin:common_newsletter_add")
        resp = self.client.post(
            add_url, {"email": "newsub@example.com"}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Newsletter.objects.filter(
            email="newsub@example.com").exists())

    def test_admin_search_works(self):
        """Search should filter by email when using search box."""
        Newsletter.objects.bulk_create([
            Newsletter(email="alpha@example.com"),
            Newsletter(email="beta@example.com"),
        ])
        changelist = reverse("admin:common_newsletter_changelist")
        resp = self.client.get(changelist, {"q": "alpha"})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "alpha@example.com")
        self.assertNotContains(resp, "beta@example.com")

    def test_admin_config_fields(self):
        """Check list_display, readonly_fields, search_fields match expectations."""
        ma = admin.site._registry[Newsletter]
        self.assertEqual(tuple(ma.list_display), ("email", "subscribed_at"))
        self.assertEqual(tuple(ma.readonly_fields), ("subscribed_at",))
        self.assertEqual(tuple(ma.search_fields), ("email",))
