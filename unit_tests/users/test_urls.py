from django.test import SimpleTestCase
from django.urls import get_resolver


class UsersURLNamespaceTests(SimpleTestCase):
    def test_users_namespace_is_included(self):
        """
        Ensure include('users.urls', namespace='users') (or apps.users) is wired.
        """
        namespaces = set(get_resolver().namespace_dict.keys())
        self.assertIn("users", namespaces,
                      "Namespace 'users' missing from project urls")
