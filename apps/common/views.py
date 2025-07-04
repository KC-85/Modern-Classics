from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, ListView
from .forms import ContactForm, NewsletterForm, FAQSearchForm
from .models import FAQ

"""
In here, we will have the views for both the contact form,
the newsletter and the success forms
"""
# Contact form view
class ContactView(FormView):
    template_name = "common/contact.html"
    form_class    = ContactForm
    success_url   = reverse_lazy("common:contact_success")

    def form_valid(self, form):
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

# FAQ list view
class FAQListView(ListView):
    model               = FAQ
    template_name       = "common/faq_list.html"
    context_object_name = "faqs"
    paginate_by         = 10

    def get_queryset(self):
        qs = super().get_queryset()
        form = FAQSearchForm(self.request.GET)
        if form.is_valid() and form.cleaned_data["query"]:
            qs = qs.filter(question__icontains=form.cleaned_data["query"])
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["search_form"] = FAQSearchForm(self.request.GET)
        return ctx
