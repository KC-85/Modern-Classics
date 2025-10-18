from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, ListView
from .forms import ContactForm, NewsletterForm, FAQSearchForm
from .models import FAQ, Newsletter

"""
In here, we will have the views for both the contact form,
the newsletter and the success forms
"""
# Contact form view


class ContactView(FormView):
    template_name = "common/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("common:contact_success")

    def form_valid(self, form):
        return super().form_valid(form)

# Contact success view (contact form)


class ContactSuccessView(TemplateView):
    template_name = "common/contact_success.html"

# Newsletter form view


class NewsletterSignupView(FormView):
    template_name = "common/newsletter.html"
    form_class = NewsletterForm
    success_url = reverse_lazy("common:newsletter_success")

    def form_valid(self, form):
        email = form.cleaned_data["email"].lower().strip()
        # idempotent-ish create
        try:
            with transaction.atomic():
                Newsletter.objects.get_or_create(email=email)
        except IntegrityError:
            pass  # unique constraint already ensured

        messages.success(
            self.request, "You're subscribed! Thanks for joining.")
        return super().form_valid(form)


class NewsletterSuccessView(TemplateView):
    template_name = "common/newsletter_success.html"

# FAQ list view


class FAQListView(ListView):
    model = FAQ
    template_name = "common/faq_list.html"
    context_object_name = "faqs"
    paginate_by = 10

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


def robots_txt(request):
    sitemap_url = request.build_absolute_uri(reverse_lazy("sitemap"))
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /accounts/",
        "Disallow: /checkout/",
        "Disallow: /trailer/",
        f"Sitemap: {sitemap_url}",
        "",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
