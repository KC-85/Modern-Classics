# Database models (Postgres)

# Order models
from django.db import models
from django.conf import settings
from apps.showroom.models import Car

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending',   'Pending'),
        ('paid',      'Paid'),
        ('shipped',   'Shipped'),
        ('completed', 'Completed'),
        ('canceled',  'Canceled'),
    ]

    user         = models.ForeignKey(
                       settings.AUTH_USER_MODEL,
                       on_delete=models.CASCADE,
                       related_name="orders"
                   )
    status       = models.CharField(
                       max_length=10,
                       choices=STATUS_CHOICES,
                       default='pending'
                   )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_session_id = models.CharField(
                       max_length=255,
                       blank=True,
                       help_text="Stripe Checkout session ID"
                   )
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.pk} by {self.user.username} ({self.get_status_display()})"

class OrderItem(models.Model):
    order      = models.ForeignKey(
                      Order,
                      on_delete=models.CASCADE,
                      related_name="items"
                  )
    car        = models.ForeignKey(
                      Car,
                      on_delete=models.PROTECT,
                      related_name="order_items"
                  )
    quantity   = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} × {self.car} @ {self.unit_price}"

    @property
    def line_total(self):
        return self.quantity * self.unit_price
