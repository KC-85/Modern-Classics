# apps/checkout/utils.py
from decimal import Decimal
from django.conf import settings

def compute_delivery(subtotal: Decimal) -> Decimal:
    """
    Example policy:
      - Free delivery when subtotal >= FREE_DELIVERY_THRESHOLD
      - Otherwise STANDARD_DELIVERY_PERCENT % of subtotal
    """
    threshold = getattr(settings, "FREE_DELIVERY_THRESHOLD", Decimal("50.00"))
    pct       = getattr(settings, "STANDARD_DELIVERY_PERCENT", Decimal("10.0"))

    if subtotal >= threshold:
        return Decimal("0.00")

    return (subtotal * pct / Decimal("100")).quantize(Decimal("0.01"))
