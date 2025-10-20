from django.test import TestCase
from apps.common.models import Newsletter


class NewsletterModelTests(TestCase):
    def test_str_is_email(self):
        n = Newsletter.objects.create(email="a@b.com")
        self.assertEqual(str(n), "a@b.com")

    def test_unique_email_constraint(self):
        Newsletter.objects.create(email="dupe@example.com")
        with self.assertRaises(Exception):
            Newsletter.objects.create(email="dupe@example.com")

    def test_auto_now_add_and_ordering(self):
        n1 = Newsletter.objects.create(email="a1@b.com")
        n2 = Newsletter.objects.create(email="a2@b.com")
        self.assertGreater(n2.subscribed_at, n1.subscribed_at)
        self.assertEqual(list(Newsletter.objects.all()), [n2, n1])
