# apps/delivery/urls.py
from django.urls import path
from .views import (
    DeliveryOptionListView, DeliveryOptionCreateView,
    DeliveryOptionUpdateView, DeliveryOptionDeleteView,
    OrderDeliveryUpdateView
)

app_name = "delivery"

urlpatterns = [
    path("options/",                  DeliveryOptionListView.as_view(),   name="option_list"),
    path("options/add/",              DeliveryOptionCreateView.as_view(), name="option_add"),
    path("options/<int:pk>/edit/",    DeliveryOptionUpdateView.as_view(), name="option_edit"),
    path("options/<int:pk>/delete/",  DeliveryOptionDeleteView.as_view(), name="option_delete"),

    path("order/<int:pk>/delivery/",  OrderDeliveryUpdateView.as_view(),  name="order_delivery"),
]
