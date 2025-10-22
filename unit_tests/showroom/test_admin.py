from django.test import TestCase
from django.contrib import admin

from apps.showroom.models import CarMake, CarModel, Car


class ShowroomAdminRegistrationTests(TestCase):
    def test_models_registered(self):
        registry = admin.site._registry
        self.assertIn(CarMake, registry,
                      "CarMake must be registered in admin.")
        self.assertIn(CarModel, registry,
                      "CarModel must be registered in admin.")
        self.assertIn(Car, registry, "Car must be registered in admin.")
