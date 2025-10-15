from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import CarMake, CarModel, Car


class CarFilterForm(forms.Form):
    make = forms.ModelChoiceField(
        queryset=CarMake.objects.all(), required=False)
    model = forms.ModelChoiceField(
        queryset=CarModel.objects.none(), required=False)
    year_from = forms.IntegerField(required=False, label="Year from")
    year_to = forms.IntegerField(required=False, label="Year to")
    condition = forms.ChoiceField(
        choices=[("", "Any")] + Car.CONDITION_CHOICES,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "get"
        self.helper.add_input(Submit("filter", "Filter"))
        # if a make is selected, limit the models field
        make_id = self.data.get("make")
        if make_id:
            self.fields["model"].queryset = CarModel.objects.filter(
                make_id=make_id)


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = (
            "make", "model", "year",
            "specifications", "performance",
            "condition", "image", "price", "is_sold"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("save", "Save Car"))
