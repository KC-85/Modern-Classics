# apps/users/urls.py
from django.urls import path
from .views import RegisterView, ProfileView

app_name = "users"

urlpatterns = [
    # Custom registration (if you still want it)
    path("register/", RegisterView.as_view(), name="register"),

    # Profile view & edit
    path("profile/",  ProfileView.as_view(),  name="profile"),
]
