"""View logic for the common app.

Handles HTTP requests, orchestrates domain operations,
and returns rendered responses."""

from django.http import HttpResponse, JsonResponse
from django.db import transaction, IntegrityError
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import (
    FormView,
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
)
from django.core.mail import send_mass_mail
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from .forms import (
    ContactForm,
    NewsletterForm,
    FAQSearchForm,
    FAQForm,
    NewsletterEmailForm,
)
from .models import FAQ, Newsletter, NewsletterEmail

"""
In here, we will have the views for both the contact form, FAQs,
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

# Newsletter subscriber signup view


class NewsletterSignupView(FormView):
    template_name = "common/newsletter.html"
    form_class = NewsletterForm
    success_url = reverse_lazy("common:newsletter_success")

    def form_valid(self, form):
        try:
            with transaction.atomic():
                form.save()
        except IntegrityError:
            form.add_error("email", "This email is already subscribed.")
            return self.form_invalid(form)
        return super().form_valid(form)


class NewsletterSuccessView(TemplateView):
    template_name = "common/newsletter_success.html"


# Newsletter email campaign management (superuser only)
superuser_required = user_passes_test(lambda user: user.is_superuser)


@method_decorator([login_required, superuser_required], name="dispatch")
class NewsletterEmailListView(ListView):
    """List all newsletter email campaigns."""
    model = NewsletterEmail
    template_name = "common/newsletter_email_list.html"
    context_object_name = "newsletters"
    paginate_by = 10
    ordering = "-created_at"


@method_decorator([login_required, superuser_required], name="dispatch")
class NewsletterEmailCreateView(CreateView):
    """Compose a new newsletter email."""
    model = NewsletterEmail
    form_class = NewsletterEmailForm
    template_name = "common/newsletter_email_form.html"
    success_url = reverse_lazy("common:newsletter_email_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Newsletter created successfully.")
        return response


@method_decorator([login_required, superuser_required], name="dispatch")
class NewsletterEmailUpdateView(UpdateView):
    """Edit a newsletter email (only if not yet sent)."""
    model = NewsletterEmail
    form_class = NewsletterEmailForm
    template_name = "common/newsletter_email_form.html"
    success_url = reverse_lazy("common:newsletter_email_list")

    def form_valid(self, form):
        # Prevent editing of sent newsletters
        if self.object.is_sent:
            messages.error(
                self.request,
                "Cannot edit a newsletter that has already been sent.")
            return redirect("common:newsletter_email_list")
        response = super().form_valid(form)
        messages.success(self.request, "Newsletter updated successfully.")
        return response


@method_decorator([login_required, superuser_required], name="dispatch")
class NewsletterEmailDeleteView(DeleteView):
    """Delete a newsletter email (only if not yet sent)."""
    model = NewsletterEmail
    template_name = "common/newsletter_email_confirm_delete.html"
    success_url = reverse_lazy("common:newsletter_email_list")

    def delete(self, request, *args, **kwargs):
        # Prevent deletion of sent newsletters
        self.object = self.get_object()
        if self.object.is_sent:
            messages.error(
                request,
                "Cannot delete a newsletter that has already been sent.")
            return redirect("common:newsletter_email_list")
        messages.success(request, "Newsletter deleted successfully.")
        return super().delete(request, *args, **kwargs)


@method_decorator([login_required, superuser_required], name="dispatch")
class NewsletterEmailSendView(View):
    """Send a newsletter email to all subscribers."""

    def post(self, request, pk):
        newsletter = get_object_or_404(NewsletterEmail, pk=pk)

        # Check if already sent
        if newsletter.is_sent:
            messages.error(request, "This newsletter has already been sent.")
            return redirect("common:newsletter_email_list")

        # Get all active subscribers
        subscribers = Newsletter.objects.values_list("email", flat=True)
        if not subscribers.exists():
            messages.warning(request, "No subscribers to send to.")
            return redirect("common:newsletter_email_list")

        # Build email tuples for send_mass_mail
        emails = []
        for subscriber_email in subscribers:
            emails.append(
                (
                    newsletter.subject,
                    newsletter.body,
                    "noreply@modernclassics.com",
                    [subscriber_email],
                )
            )

        try:
            with transaction.atomic():
                # Send emails
                send_mass_mail(emails, fail_silently=False)

                # Mark newsletter as sent
                newsletter.status = "sent"
                newsletter.sent_at = timezone.now()
                newsletter.recipient_count = subscribers.count()
                newsletter.save()

            messages.success(
                request,
                f"Newsletter sent to {subscribers.count()} subscriber(s)."
            )
        except Exception as e:
            messages.error(
                request,
                f"Error sending newsletter: {str(e)}"
            )

        return redirect("common:newsletter_email_list")


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


@method_decorator([login_required, superuser_required], name="dispatch")
class FAQCreateView(CreateView):
    model = FAQ
    form_class = FAQForm
    template_name = "common/faq_form.html"
    success_url = reverse_lazy("common:faq_list")


@method_decorator([login_required, superuser_required], name="dispatch")
class FAQUpdateView(UpdateView):
    model = FAQ
    form_class = FAQForm
    template_name = "common/faq_form.html"
    success_url = reverse_lazy("common:faq_list")


@method_decorator([login_required, superuser_required], name="dispatch")
class FAQDeleteView(DeleteView):
    model = FAQ
    template_name = "common/faq_confirm_delete.html"
    success_url = reverse_lazy("common:faq_list")

    def form_valid(self, form):
        faq_label = str(self.object)
        response = super().form_valid(form)
        messages.success(
            self.request, f"FAQ deleted successfully: {faq_label}")
        return response


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
