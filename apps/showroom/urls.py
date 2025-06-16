# apps/showroom/urls.py
from django.urls import path
from .views import (
    CarListView, CarDetailView,
    CarCreateView, CarUpdateView, CarDeleteView
)

app_name = "showroom"

urlpatterns = [
    path("",                 CarListView.as_view(),   name="car_list"),
    path("<int:pk>/",        CarDetailView.as_view(), name="car_detail"),
    path("add/",             CarCreateView.as_view(), name="car_add"),
    path("<int:pk>/edit/",   CarUpdateView.as_view(), name="car_edit"),
    path("<int:pk>/delete/", CarDeleteView.as_view(), name="car_delete"),
]
