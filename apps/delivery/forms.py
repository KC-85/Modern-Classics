# apps/delivery/forms.py

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class DeliveryDistanceForm(forms.Form):
    delivery_distance = forms.IntegerField(
        min_value=0,
        label="Delivery distance (miles)",
        help_text="Enter the number of miles from our showroom to your address",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Crispy form helper for consistent styling
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("save", "Save Distance"))
