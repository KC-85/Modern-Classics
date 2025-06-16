from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from .forms import UserRegistrationForm, UserProfileForm

"""
These here, are the views for creating a user profile
"""

# View to create a profile
@method_decorator(login_required, name="dispatch")
class ProfileView(updateView):
    template_name = "users/profile.html"
    form_class    = UserProfileForm
    success_url   reverse_lazy("users:profile")

    def get_object(self):
        return self.request.user

# Profile success view
class ProfileSuccessView(TemplateView):
    template_name = "users/profile_success.html"