from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import CartItem

class AddToCartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ("quantity",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("add", "Add to Cart"))

class UpdateCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("update", "Update Quantity"))
