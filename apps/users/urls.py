"""URL routing for the users app.

Maps request paths to view callables and namespaced route names."""

# apps/users/urls.py
from django.urls import path
from .views import ProfileLandingView, ProfileView, ProfileDeleteView

app_name = "users"

urlpatterns = [
    # Profile pages
    path("profile/", ProfileLandingView.as_view(), name="profile"),
    path("profile/edit/", ProfileView.as_view(), name="profile_edit"),
    path(
        "profile/delete/", ProfileDeleteView.as_view(), name="profile_delete"),
]
