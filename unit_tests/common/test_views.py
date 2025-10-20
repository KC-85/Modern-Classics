from django.test import TestCase
from django.urls import reverse
from apps.common.models import Newsletter


class NewsletterSignupViewTests(TestCase):
    def test_get_renders_form(self):
        url = reverse("common:newsletter")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Newsletter")

    def test_post_valid_redirects_to_success_and_creates_record(self):
        url = reverse("common:newsletter")
        resp = self.client.post(
            url, {"email": "ok@example.com", "consent": True})
        self.assertRedirects(resp, reverse("common:newsletter_success"))
        self.assertTrue(Newsletter.objects.filter(
            email="ok@example.com").exists())

    def test_post_duplicate_stays_on_form_with_error(self):
        Newsletter.objects.create(email="dupe@example.com")
        url = reverse("common:newsletter")
        resp = self.client.post(
            url, {"email": "dupe@example.com", "consent": True})
        # Expect form to re-render (200) with an error message you add in the view
        self.assertEqual(resp.status_code, 200)
        # Match your view’s error text exactly:
        self.assertContains(resp, "already subscribed",
                            status_code=200, html=False)


class NewsletterSuccessViewTests(TestCase):
    def test_success_page_renders(self):
        url = reverse("common:newsletter_success")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        # Your template shows “You’re subscribed!”
        text = resp.content.decode()
        self.assertTrue(
            ("You're subscribed!" in text) or (
                "You&#x27;re subscribed!" in text),
            "Success copy not found"
        )
