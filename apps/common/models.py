# Database models (Postgres)

# Newsletter
class Newsletter(models.Model):
    email         = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-subscribed_at",)

    def __str__(self):
        return self.email

# Contact
class Contact(models.Model):
    name        = models.CharField(max_length=100)
    email       = models.EmailField()
    message     = models.TextField()
    date_sent   = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ("-date_sent",)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

# FAQs
class FAQ(models.Model):
    question    = models.CharField(max_length=255)
    answer      = models.TextField()
    order       = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("order", "question")

    def __str__(self):
        return self.question
