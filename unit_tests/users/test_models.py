from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UsersModelTests(TestCase):
    def test_create_user_minimal(self):
        u = User.objects.create_user(
            username="u1",
            password="x",
        )
        self.assertTrue(u.is_active)
        self.assertFalse(u.is_staff)
        self.assertFalse(u.is_superuser)
        self.assertEqual(str(u), "u1")

    def test_create_superuser(self):
        su = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="x",
        )
        self.assertTrue(su.is_active)
        self.assertTrue(su.is_staff)
        self.assertTrue(su.is_superuser)
        self.assertEqual(str(su), "admin")

    def test_email_is_not_unique_by_default(self):
        # Your model does NOT set unique=True on email; creating duplicates should be allowed.
        User.objects.create_user(
            username="a", email="dupe@example.com", password="x")
        User.objects.create_user(
            username="b", email="dupe@example.com", password="x")
        self.assertEqual(User.objects.filter(
            email="dupe@example.com").count(), 2)

    def test_str_is_human_readable(self):
        u = User.objects.create_user(
            username="pretty", email="pretty@example.com", password="x")
        self.assertEqual(str(u), "pretty")
