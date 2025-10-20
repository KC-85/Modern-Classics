from django.test import TestCase
from django.urls import reverse
from apps.common.forms import NewsletterForm
from apps.common.models import Newsletter


class NewsletterFormTests(TestCase):
    def test_valid_email_creates_instance(self):
        form = NewsletterForm(
            data={"email": "ok@example.com", "consent": True})
        self.assertTrue(form.is_valid(), form.errors)
        inst = form.save()
        self.assertIsInstance(inst, Newsletter)
        self.assertEqual(inst.email, "ok@example.com")

    def test_rejects_totally_invalid_email(self):
        form = NewsletterForm(data={"email": "not-an-email", "consent": True})
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_duplicate_email_is_invalid(self):
        Newsletter.objects.create(email="dupe@example.com")
        form = NewsletterForm(
            data={"email": "dupe@example.com", "consent": True})
        # Depending on your form, you may or may not catch duplicate at form level.
        # We at least expect the form to be invalid if you validate uniqueness.
        if form.is_valid():
            # If the form allows it, saving must raise due to DB unique constraint.
            with self.assertRaises(Exception):
                form.save()
        else:
            self.assertIn("email", form.errors)
