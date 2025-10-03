from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE, related_name="models"
    )
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ("make", "name")

    def __str__(self):
        return f"{self.make.name} {self.name}"

class Car(models.Model):
    CONDITION_CHOICES = [
        ("poor", "Poor"),
        ("fair", "Fair"),
        ("good", "Good"),
        ("excellent", "Excellent"),
    ]

    make           = models.ForeignKey(
                        CarMake, on_delete=models.CASCADE, related_name="cars"
                     )
    model          = models.ForeignKey(
                        CarModel, on_delete=models.CASCADE, related_name="cars"
                     )
    year           = models.PositiveIntegerField()
    specifications = models.TextField(help_text="Full spec sheet or description")
    performance    = models.CharField(
                        max_length=255,
                        help_text="E.g. 0–60 in 5.2s; 155 mph top speed"
                     )
    condition      = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    image          = CloudinaryField("image", blank=True, null=True)
    price          = models.DecimalField(max_digits=10, decimal_places=2)
    slug           = models.SlugField(max_length=150, unique=True, blank=True)
    is_sold        = models.BooleanField(default=False)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-year", "make__name", "model__name")

    def save(self, *args, **kwargs):
        if not self.slug:
            base = f"{self.make.name}-{self.model.name}-{self.year}"
            self.slug = slugify(base)[:150]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("showroom:car_detail", kwargs={"slug": self.slug})

    def __str__(self):
        sold = " (SOLD)" if self.is_sold else ""
        return f"{self.make.name} {self.model.name} ({self.year}) — £{self.price}{sold}"
