# apps/users/urls.py
from django.urls import path
from .views import ProfileView

app_name = "users"

urlpatterns = [
    # Profile view & edit
    path("profile/",  ProfileView.as_view(),  name="profile"),
]
