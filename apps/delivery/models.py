from django.db import models
from apps.orders.models import Order

class DeliveryOption(models.Model):
    name        = models.CharField(max_length=100)
    fee         = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} (${self.fee})"

class OrderDelivery(models.Model):
    order       = models.OneToOneField(Order, on_delete=models.CASCADE)
    option      = models.ForeignKey(DeliveryOption, on_delete=models.PROTECT)
    tracking_id = models.CharField(max_length=100, blank=True)
    shipped_at  = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Delivery for Order #{self.order.pk}"
