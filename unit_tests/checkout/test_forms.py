from django.test import TestCase
from apps.checkout.forms import OrderForm


class OrderFormTests(TestCase):
    def test_widget_classes_and_autofocus(self):
        form = OrderForm()
        for name, field in form.fields.items():
            self.assertIn("class", field.widget.attrs)
            self.assertIn("stripe-style-input", field.widget.attrs["class"])
        self.assertEqual(
            form.fields["full_name"].widget.attrs.get("autofocus"), True)

    def test_labels_prefixed_for_required(self):
        # By default most are required; 'country' is skipped for placeholder/label tweak
        form = OrderForm()
        for name, field in form.fields.items():
            if name != "country" and field.required:
                self.assertTrue(field.label.startswith("* "))
