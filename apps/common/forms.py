from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ContactForm(forms.Form):
    name    = forms.CharField(max_length=100)
    email   = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("send", "Send Message"))

class NewsletterForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("subscribe", "Subscribe"))

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if Newsletter.objects.filter(email__iexact=email).exists():
            raise ValidationError("This email is already subscribed.")
        return email

class FAQSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        label="Search FAQs",
        widget=forms.TextInput(attrs={"placeholder": "Search FAQs…"})
    )
