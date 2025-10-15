# apps/checkout/forms.py

from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country',
            'county',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        # Autofocus on the first field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        for name, field in self.fields.items():
            # Skip placeholder logic (select widget)
            if name != 'country':
                if field.required:
                    field.label = f'* {field.label}'
            # Apply a common CSS class for Stripe styling
            field.widget.attrs['class'] = 'stripe-style-input'
