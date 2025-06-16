# apps/common/urls.py
from django.urls import path
from .views import (
    ContactView, ContactSuccessView,
    NewsletterSignupView, NewsletterSuccessView,
    FAQListView
)

app_name = "common"

urlpatterns = [
    path("contact/",             ContactView.as_view(),            name="contact"),
    path("contact/success/",     ContactSuccessView.as_view(),     name="contact_success"),
    path("newsletter/",          NewsletterSignupView.as_view(),   name="newsletter"),
    path("newsletter/success/",  NewsletterSuccessView.as_view(),  name="newsletter_success"),
    path("faq/",                 FAQListView.as_view(),            name="faq_list"),
]
