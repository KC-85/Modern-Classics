"""Database models for the common app.

Declares persisted entities, relationships, and model-level business rules."""

# Database models (Postgres)
from django.db import models
from django.utils import timezone


# Newsletter subscriber list
class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-subscribed_at",)
        constraints = [
            models.UniqueConstraint(
                fields=["email"],
                name="unique_newsletter_email"
            )
        ]

    def __str__(self):
        return self.email


# Newsletter email campaigns
class NewsletterEmail(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("scheduled", "Scheduled"),
        ("sent", "Sent"),
    ]

    subject = models.CharField(max_length=255)
    body = models.TextField(
        help_text="HTML or plain text body of the newsletter")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField(
        null=True, blank=True, help_text="When to send (optional)")
    sent_at = models.DateTimeField(
        null=True, blank=True, help_text="Timestamp when email was sent")
    recipient_count = models.PositiveIntegerField(
        default=0,
        help_text="Number of subscribers who received it")

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.subject} ({self.get_status_display()})"

    @property
    def is_sent(self) -> bool:
        return self.status == "sent"


# Contact
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ("-date_sent",)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


# FAQs
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(
        default=0, help_text="Lower numbers appear first")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("order", "question")

    def __str__(self):
        return self.question
