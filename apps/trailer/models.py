from django.conf import settings
from django.db import models
from apps.showroom.models import Car

class Cart(models.Model):
    user     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart #{self.pk} for {self.user}"

class CartItem(models.Model):
    cart     = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    car      = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("cart", "car")

    def __str__(self):
        return f"{self.quantity}× {self.car}"
