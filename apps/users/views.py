"""View logic for the users app.

Handles HTTP requests, orchestrates domain operations, and returns rendered responses."""

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView, DeleteView
from django.shortcuts import redirect
from .forms import UserProfileForm
from .models import CustomUser

"""
These here, are the views for creating a user profile
"""

# Profile landing page
@method_decorator(login_required, name="dispatch")
class ProfileLandingView(TemplateView):
    template_name = "users/profile_overview.html"


# View to edit a profile
@method_decorator(login_required, name="dispatch")
class ProfileView(UpdateView):
    template_name = "users/profile.html"
    form_class    = UserProfileForm
    success_url   = reverse_lazy("users:profile")

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your profile has been updated successfully.")
        return response


@method_decorator(login_required, name="dispatch")
class ProfileDeleteView(DeleteView):
    model = CustomUser
    template_name = "users/profile_confirm_delete.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        confirmation_value = request.POST.get("confirm_identity", "").strip()
        allowed_values = {user.username}

        if user.email:
            allowed_values.add(user.email)

        if confirmation_value not in allowed_values:
            messages.error(
                request,
                "Confirmation failed. Type your exact username or email to delete your profile."
            )
            return redirect("users:profile_delete")

        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        username = user.username
        user.delete()
        logout(request)
        messages.success(request, f"Your profile has been deleted successfully. Goodbye, {username}.")
        return redirect(self.success_url)

# Profile success view
class ProfileSuccessView(TemplateView):
    template_name = "users/profile_success.html"
