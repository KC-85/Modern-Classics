from importlib import import_module
from django import forms
from django.test import TestCase


class TrailerFormsSmokeTests(TestCase):
    def test_all_form_classes_are_forms(self):
        """
        If you add forms (e.g., QuantityForm), ensure they subclass Form/ModelForm.
        If there are no forms yet, this will pass.
        """
        try:
            mod = import_module("apps.trailer.forms")
        except ModuleNotFoundError:
            self.skipTest("apps.trailer.forms not found")

        form_classes = [
            getattr(mod, n)
            for n in dir(mod)
            if n.endswith("Form") and isinstance(getattr(mod, n), type)
        ]
        for cls in form_classes:
            self.assertTrue(
                issubclass(cls, (forms.BaseForm, forms.ModelForm, forms.Form)),
                f"{cls.__name__} must subclass a Django Form",
            )
