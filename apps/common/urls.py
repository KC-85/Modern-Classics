"""URL routing for the common app.

Maps request paths to view callables and namespaced route names."""

# apps/common/urls.py
from django.urls import path
from .views import (
    ContactView, ContactSuccessView,
    NewsletterSignupView, NewsletterSuccessView,
    NewsletterEmailListView, NewsletterEmailCreateView,
    NewsletterEmailUpdateView,
    NewsletterEmailDeleteView, NewsletterEmailSendView,
    FAQListView, FAQCreateView, FAQUpdateView, FAQDeleteView
)

app_name = "common"

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),
    path(
        "contact/success/", ContactSuccessView.as_view(),
        name="contact_success"),
    path("newsletter/", NewsletterSignupView.as_view(), name="newsletter"),
    path(
        "newsletter/success/", NewsletterSuccessView.as_view(),
        name="newsletter_success"),

    # Newsletter email management (superuser)
    path(
        "newsletter-email/",
        NewsletterEmailListView.as_view(), name="newsletter_email_list"),
    path(
        "newsletter-email/create/",
        NewsletterEmailCreateView.as_view(), name="newsletter_email_create"),
    path(
        "newsletter-email/<int:pk>/edit/", NewsletterEmailUpdateView.as_view(),
        name="newsletter_email_edit"),
    path(
        "newsletter-email/<int:pk>/delete/",
        NewsletterEmailDeleteView.as_view(), name="newsletter_email_delete"),
    path(
        "newsletter-email/<int:pk>/send/",
        NewsletterEmailSendView.as_view(), name="newsletter_email_send"),

    path("faq/", FAQListView.as_view(), name="faq_list"),
    path("faq/add/", FAQCreateView.as_view(), name="faq_create"),
    path("faq/<int:pk>/edit/", FAQUpdateView.as_view(), name="faq_edit"),
    path("faq/<int:pk>/delete/", FAQDeleteView.as_view(), name="faq_delete"),
]
