# apps/orders/models.py

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
    total_amount      = models.DecimalField(max_digits=10, decimal_places=2)

    # delivery integration (string ref to avoid circular import)
    delivery_option   = models.ForeignKey(
                            'delivery.DeliveryOption',
                            null=True,
                            blank=True,
                            on_delete=models.SET_NULL,
                            related_name="orders"
                        )

    @property
    def delivery_fee(self):
        return self.delivery_option.price if self.delivery_option else 0

    @property
    def total_with_delivery(self):
        return self.total_amount + self.delivery_fee

    # Stripe references
    stripe_session_id = models.CharField(
                            max_length=255,
                            blank=True,
                            null=True,
                            help_text="Stripe Checkout Session ID"
                        )
    stripe_intent_id  = models.CharField(
                            max_length=255,
                            blank=True,
                            null=True,
                            help_text="Stripe PaymentIntent ID"
                        )

    # Post-payment details
    paid_amount       = models.DecimalField(
                            max_digits=10,
                            decimal_places=2,
                            blank=True, null=True
                        )
    currency          = models.CharField(
                            max_length=3,
                            blank=True, null=True,
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
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} × {self.car} @ £{self.unit_price:.2f}"

    @property
    def line_total(self):
        return self.quantity * self.unit_price
