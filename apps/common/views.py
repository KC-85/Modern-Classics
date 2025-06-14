from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import ContactForm, NewsletterForm

"""
In here, we will have the views for both the contact form,
the newsletter and the success forms
"""
# Contact form view
class ContactView(FormView):
    template_name = "common/contact.html"
    form_class    = ContactForm
    success_url   = reverse_lazy("common:contact_success")

    def form_valid(self, form)
        return super().form_valid(form)

# Contact success view (contact form)
class ContactSuccessView(TemplateView):
    template_name = "common/contact_success.html"

# Newsletter form view
class NewsletterSignupView(FormView):
    template_name = "common/newsletter.html"
    form_class    = NewsletterForm
    success_url   = reverse_lazy("common:newsletter_success")

    def form_valid(self, form):
        return super().form_valid(form)

# Newsletter success view
class NewsletterSuccessView(TemplateView):
    template_name = "common/newsletter_success.html"
