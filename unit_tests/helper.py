from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class BaseTestCase(TestCase):
    def make_user(self, **kw):
        data = dict(username="u", email="u@example.com", password="pass12345")
        data.update(kw)
        return User.objects.create_user(**{k: data[k] for k in ("username", "email", "password")})

    def make_superuser(self, **kw):
        data = dict(username="admin", email="admin@example.com",
                    password="adminpass")
        data.update(kw)
        return User.objects.create_superuser(**{k: data[k] for k in ("username", "email", "password")})

    def login(self, user, password=None):
        self.client.logout()
        ok = self.client.login(username=user.username,
                               password=password or "pass12345")
        self.assertTrue(ok)

    def r(self, name, **kwargs):
        return reverse(name, kwargs=kwargs) if kwargs else reverse(name)
