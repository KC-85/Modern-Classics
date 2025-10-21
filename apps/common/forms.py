from django import forms
from django.core.exceptions import ValidationError
from .models import Newsletter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("send", "Send Message"))


class NewsletterForm(forms.ModelForm):
    consent = forms.BooleanField(
        required=True,
        label="I agree to receive Modern Classics emails."
    )

    class Meta:
        model = Newsletter
        fields = ["email", "consent"]

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip()
        # case-insensitive check to avoid duplicates with different casing
        if Newsletter.objects.filter(email__iexact=email).exists():
            raise ValidationError("This email is already subscribed.")
        return email

    def save(self, commit=True):
        # Only store the email in the model
        instance = Newsletter(email=self.cleaned_data["email"])
        if commit:
            instance.save()
        return instance


class FAQSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        label="Search FAQs",
        widget=forms.TextInput(attrs={"placeholder": "Search FAQs…"})
    )
