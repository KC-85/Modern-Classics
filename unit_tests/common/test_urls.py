from django.test import SimpleTestCase
from django.urls import resolve, reverse


class URLResolutionTests(SimpleTestCase):
    def test_newsletter_routes(self):
        self.assertEqual(reverse("common:newsletter"), "/common/newsletter/")
        self.assertEqual(reverse("common:newsletter_success"),
                         "/common/newsletter/success/")
        self.assertTrue(
            resolve("/common/newsletter/").view_name.endswith("newsletter"))
        self.assertTrue(
            resolve("/common/newsletter/success/").view_name.endswith("newsletter_success"))

    def test_misc_routes_exist(self):
        # Adjust these paths/names to your actual routes
        for name in ["common:faq_list", "common:contact"]:
            # just ensure reversing doesn’t throw
            reverse(name)
