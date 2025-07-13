# apps/orders/models.py

import math
from django.db import models
from django.conf import settings
from apps.showroom.models import Car


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING   = 'pending',   'Pending'
        PAID      = 'paid',      'Paid'
        SHIPPED   = 'shipped',   'Shipped'
        COMPLETED = 'completed', 'Completed'
        CANCELED  = 'canceled',  'Canceled'

    user              = models.ForeignKey(
                            settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE,
                            related_name="orders"
                        )
    status            = models.CharField(
                            max_length=10,
                            choices=Status.choices,
                            default=Status.PENDING
                        )
    total_amount      = models.DecimalField(
                            max_digits=10,
                            decimal_places=2
                        )

    # delivery distance in miles
    delivery_distance = models.PositiveIntegerField(
                            null=True, blank=True,
                            help_text="Miles from showroom to delivery address"
                        )

    @property
    def delivery_fee(self):
        """
        Free for <=25 miles,
        £50 for 26–100 miles,
        then +£10 for each complete 50-mile block beyond 100:
          101–149 → £50
          150–199 → £60
          200–249 → £70
          etc.
        """
        dist = self.delivery_distance or 0
        if dist <= 25:
            return 0
        if dist <= 100:
            return 50
        extra = dist - 100
        chunks = extra // 50
        return 50 + (chunks * 10)

    @property
    def total_with_delivery(self):
        return self.total_amount + self.delivery_fee

    # Stripe references
    stripe_session_id = models.CharField(
                            max_length=255, blank=True, null=True,
                            help_text="Stripe Checkout Session ID"
                        )
    stripe_intent_id  = models.CharField(
                            max_length=255, blank=True, null=True,
                            help_text="Stripe PaymentIntent ID"
                        )

    # Post-payment details
    paid_amount       = models.DecimalField(
                            max_digits=10, decimal_places=2,
                            blank=True, null=True
                        )
    currency          = models.CharField(
                            max_length=3, blank=True, null=True,
                            help_text="ISO currency code, e.g. GBP, USD"
                        )

    # Shipping info captured at checkout
    shipping_name     = models.CharField(max_length=255, blank=True, null=True)
    shipping_address  = models.JSONField(blank=True, null=True)

    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)

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
    unit_price = models.DecimalField(
                     max_digits=10, decimal_places=2
                 )

    def __str__(self):
        return f"{self.quantity} × {self.car} @ £{self.unit_price:.2f}"

    @property
    def line_total(self):
        return self.quantity * self.unit_price
