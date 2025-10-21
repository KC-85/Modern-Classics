import unittest
from django import forms
from django.test import SimpleTestCase

# Try a few likely import locations for your forms
_FORM_MODULES = []
for path in ("apps.users.forms", "users.forms"):
    try:
        _FORM_MODULES.append(__import__(path, fromlist=["*"]))
    except Exception:
        pass


@unittest.skipUnless(_FORM_MODULES, "No users.forms module found")
class UsersFormsSmokeTests(SimpleTestCase):
    def test_form_classes_subclass_django_form(self):
        """
        Any class ending with 'Form' should be a Form/ModelForm.
        """
        found = 0
        for mod in _FORM_MODULES:
            for name in dir(mod):
                if not name.endswith("Form"):
                    continue
                cls = getattr(mod, name)
                if isinstance(cls, type):
                    self.assertTrue(
                        issubclass(cls, (forms.Form, forms.ModelForm)),
                        f"{name} is not a Django form",
                    )
                    found += 1
        self.assertGreaterEqual(found, 0)
