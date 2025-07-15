import uuid
from decimal import Decimal
from django.conf import settings
from django.db import models
from django.utils import timezone

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

    # snapshot of the cart at time of purchase
    original_trailer = JSONField()

    # Stripe
    stripe_pid      = models.CharField(max_length=254, blank=True)

    class Meta:
        ordering = ["-date"]

    def _calculate_totals(self):
        self.order_total = sum(
            item.lineitem_total for item in self.lineitems.all()
        )
        # you can adjust delivery logic here, or inject from orders.Order
        self.grand_total = self.order_total + self.delivery_cost

    def save(self, *args, **kwargs):
        # first save to get a PK (and allow inlines to attach)
        new = self.pk is None
        super().save(*args, **kwargs)
        # then recalc totals if not brand-new
        self._calculate_totals()
        super().save(update_fields=["order_total", "grand_total"])

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
                       on_delete=models.PROTECT
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
