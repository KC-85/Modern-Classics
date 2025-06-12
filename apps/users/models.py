# apps/users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

class CustomUser(AbstractUser):
    """Extends Django’s default User with profile/contact info."""

    # Contact details
    phone_number   = models.CharField(max_length=20, blank=True)
    date_of_birth  = models.DateField(null=True, blank=True)

    # Shipping/billing address
    address_line1  = models.CharField("Address line 1", max_length=255, blank=True)
    address_line2  = models.CharField("Address line 2", max_length=255, blank=True)
    city           = models.CharField(max_length=100, blank=True)
    postal_code    = models.CharField("Postal / ZIP code", max_length=20, blank=True)
    country        = models.CharField(max_length=100, blank=True)

    # Optional profile image via Cloudinary
    profile_image  = CloudinaryField("profile image", blank=True, null=True)

    def __str__(self):
        return self.username
