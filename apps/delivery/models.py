from django.db import models

class DeliveryOption(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    price       = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} — £{self.price}"

class OrderDelivery(models.Model):
    order       = models.OneToOneField(
                      "checkout.Order",
                      on_delete=models.CASCADE,
                      related_name="delivery"
                  )
    option      = models.ForeignKey(
                      DeliveryOption,
                      on_delete=models.PROTECT,
                      related_name="order_deliveries"
                  )
    tracking_id = models.CharField(max_length=100, blank=True)
    shipped_at  = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Delivery for {self.order.order_number}: {self.option.name}"
