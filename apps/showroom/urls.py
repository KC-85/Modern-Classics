# apps/showroom/urls.py
from django.urls import path
from .views import (
    CarListView, CarDetailView,
    CarCreateView, CarUpdateView, CarDeleteView
)

app_name = "showroom"

urlpatterns = [
    path("",                    CarListView.as_view(),   name="car_list"),
    path("add/",                CarCreateView.as_view(), name="car_create"),
    path("<slug:slug>/edit/",   CarUpdateView.as_view(), name="car_edit"),
    path("<slug:slug>/delete/", CarDeleteView.as_view(), name="car_delete"),
    path("<slug:slug>/",        CarDetailView.as_view(), name="car_detail"),
]
