"""Form classes for the users app.

Defines validation rules and form field behavior for user-submitted data."""

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("register", "Sign Up"))

class UserProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username", "email",
            "first_name", "last_name",
            "phone_number", "date_of_birth",
            "address_line1", "address_line2",
            "city", "postal_code", "country",
            "profile_image",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # remove the password field entirely
        self.fields.pop("password", None)

        # Add Bootstrap styling to all fields
        for field in self.fields:
            if field == "date_of_birth":
                self.fields[field].widget.attrs.update({
                    "type": "date",
                    "class": "form-control"
                })
            elif field == "profile_image":
                self.fields[field].widget.attrs.update({
                    "class": "form-control"
                })
            else:
                self.fields[field].widget.attrs.update({
                    "class": "form-control"
                })

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("update", "Update Profile"))
