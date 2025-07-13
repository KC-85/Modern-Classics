# checkout/models.py
import uuid
from decimal import Decimal

from django.conf import settings
from django.db import models
from django.utils import timezone

# If you’re on Django ≥3.1 you can use models.JSONField directly:
try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField

from apps.showroom.models import Car


class Order(models.Model):
    order_number    = models.UUIDField(default=uuid.uuid4,
                                       editable=False,
                                       unique=True)
    user            = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.SET_NULL,
                        null=True, blank=True
                      )
    date            = models.DateTimeField(default=timezone.now)
    full_name       = models.CharField(max_length=254)
    email           = models.EmailField()
    phone_number    = models.CharField(max_length=20)
    country         = models.CharField(max_length=40)
    postcode        = models.CharField(max_length=20)
    town_or_city    = models.CharField(max_length=40)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, blank=True)
    county          = models.CharField(max_length=80, blank=True)

    delivery_cost   = models.DecimalField(max_digits=6,
                                          decimal_places=2,
                                          default=Decimal("0.00"))
    order_total     = models.DecimalField(max_digits=10,
                                          decimal_places=2,
                                          default=Decimal("0.00"))
    grand_total     = models.DecimalField(max_digits=10,
                                          decimal_places=2,
                                          default=Decimal("0.00"))

    # store snapshot of the cart/trailer
    original_trailer = JSONField()

    # Stripe payment intent ID
    stripe_pid      = models.CharField(max_length=254, blank=True)

    def _calculate_totals(self):
        """
        Sum up all lineitem_total, add delivery, set grand_total.
        """
        self.order_total = sum(
            item.lineitem_total for item in self.lineitems.all()
        )
        # you can customise delivery logic here
        if self.order_total < Decimal("100.00"):
            self.delivery_cost = Decimal("5.00")
        else:
            self.delivery_cost = Decimal("0.00")
        self.grand_total = self.order_total + self.delivery_cost

    def save(self, *args, **kwargs):
        # on first save (no PK yet) skip totals calc; after that, always recalc
        super().save(*args, **kwargs)
        self._calculate_totals()
        super().save(update_fields=["order_total",
                                    "delivery_cost",
                                    "grand_total"])

    def __str__(self):
        return str(self.order_number)


class OrderLineItem(models.Model):
    order          = models.ForeignKey(
                       Order,
                       on_delete=models.CASCADE,
                       related_name="lineitems"
                     )
    car            = models.ForeignKey(
                       Car,
                       on_delete=models.CASCADE
                     )
    quantity       = models.PositiveIntegerField(default=1)
    unit_price     = models.DecimalField(max_digits=10,
                                         decimal_places=2)
    lineitem_total = models.DecimalField(max_digits=10,
                                         decimal_places=2,
                                         editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} × {self.car}"
