from django.conf import settings
from django.db import models
from django.db.models import Sum, F, DecimalField
from apps.showroom.models import Car

class Cart(models.Model):
    user       = models.OneToOneField(
                     settings.AUTH_USER_MODEL,
                     on_delete=models.CASCADE,
                     related_name="cart"
                 )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart #{self.pk} for {self.user}"

    @property
    def total_amount(self):
        agg = self.items.aggregate(
            total=Sum(
                F("quantity") * F("car__price"),
                output_field=DecimalField(),
            )
        )["total"]
        return agg or 0

    def clear(self):
        self.items.all().delete()

class CartItem(models.Model):
    cart     = models.ForeignKey(
                   Cart, related_name="items", on_delete=models.CASCADE
               )
    car      = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("cart", "car")

    def __str__(self):
        return f"{self.quantity}× {self.car}"
