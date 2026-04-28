"""Form classes for the common app.

Defines validation rules and form field behavior for user-submitted data."""

from django import forms
from django.core.exceptions import ValidationError
from .models import FAQ, Newsletter, NewsletterEmail
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


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ["question", "answer", "order"]


class NewsletterEmailForm(forms.ModelForm):
    """Form for composing and managing newsletter campaigns."""

    class Meta:
        model = NewsletterEmail
        fields = ["subject", "body", "status", "scheduled_at"]
        widgets = {
            "subject": forms.TextInput(attrs={
                "placeholder": "Newsletter subject line",
                "class": "form-control"
            }),
            "body": forms.Textarea(attrs={
                "placeholder": "Newsletter body (HTML supported)",
                "class": "form-control",
                "rows": 15
            }),
            "status": forms.Select(attrs={"class": "form-select"}),
            "scheduled_at": forms.DateTimeInput(attrs={
                "type": "datetime-local",
                "class": "form-control"
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get("status")
        scheduled_at = cleaned_data.get("scheduled_at")

        # If scheduling, require a scheduled_at time
        if status == "scheduled" and not scheduled_at:
            raise ValidationError(
                "Scheduled newsletters must have a scheduled time.")

        return cleaned_data
