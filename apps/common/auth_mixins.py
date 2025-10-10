# common/auth_mixins.py
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from functools import wraps
from django.urls import reverse_lazy

class LoginRequiredMessageMixin(LoginRequiredMixin):
    login_url = reverse_lazy("account_login")   # allauth login
    redirect_field_name = "next"

    def handle_no_permission(self):
        # Only show the prompt if truly unauthenticated
        if not self.request.user.is_authenticated:
            messages.info(self.request, "Please sign in or sign up to continue the purchase.")
        return super().handle_no_permission()
        # Note: If the user is authenticated but lacks permissions,
        # the default behavior (403 Forbidden) will occur without a message.

def login_required_with_message(view_func):
    """
    FBV version:
    - If user is anonymous, queue a friendly banner message
    - Redirect to allauth login, preserving ?next=
    """
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, BANNER_TEXT)
        # delegate to Django's login_required with our login_url
        protected = login_required(login_url=reverse_lazy("account_login"))(view_func)
        return protected(request, *args, **kwargs)
    return _wrapped
