from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import DeliveryOption, OrderDelivery

class DeliveryOptionForm(forms.ModelForm):
    class Meta:
        model = DeliveryOption
        fields = ("name", "fee", "description")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("save", "Save Option"))

class OrderDeliveryForm(forms.ModelForm):
    class Meta:
        model = OrderDelivery
        fields = ("option", "tracking_id", "shipped_at")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("update", "Update Delivery"))
