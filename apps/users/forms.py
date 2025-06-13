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
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("update", "Update Profile"))
