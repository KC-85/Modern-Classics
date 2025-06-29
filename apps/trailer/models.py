from django.conf import settings
from django.db import models
from django.db.models import Sum, F, DecimalField
from apps.showroom.models import Car

class Cart(models.Model):
    user    = models.ForeignKey(
                  settings.AUTH_USER_MODEL,
                  on_delete=models.CASCADE,
                  related_name="cart"
              )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart #{self.pk} for {self.user}"

    @property
    def total_amount(self):
        """
        Sum up each item's quantity * unit price.
        Uses a DB aggregate so it’s fast even if you have lots of items.
        """
        agg = self.items.aggregate(
            total=Sum(
                F("quantity") * F("car__price"),
                output_field=DecimalField(),
            )
        )["total"]
        return agg or 0


class CartItem(models.Model):
    cart     = models.ForeignKey(
                   Cart,
                   related_name="items",
                   on_delete=models.CASCADE
               )
    car      = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("cart", "car")

    def __str__(self):
        return f"{self.quantity}× {self.car}"
