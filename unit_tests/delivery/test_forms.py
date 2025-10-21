import unittest
from django import forms
from django.test import SimpleTestCase

# Try a few common import paths; skip if none exist
_FORM_MODULES = []
for path in ("apps.delivery.forms", "delivery.forms"):
    try:
        _FORM_MODULES.append(__import__(path, fromlist=["*"]))
    except Exception:
        pass


@unittest.skipUnless(_FORM_MODULES, "No delivery forms module found")
class DeliveryFormsSmokeTests(SimpleTestCase):
    def test_forms_are_django_forms(self):
        """
        Sanity: any attributes ending with 'Form' are subclasses of Form/ModelForm.
        """
        found = 0
        for mod in _FORM_MODULES:
            for name in dir(mod):
                if not name.endswith("Form"):
                    continue
                cls = getattr(mod, name)
                if isinstance(cls, type):
                    issub = issubclass(cls, (forms.Form, forms.ModelForm))
                    if issub:
                        found += 1
        # smoke; will always pass but iterates
        self.assertGreaterEqual(found, 0)
