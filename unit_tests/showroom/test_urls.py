from django.test import SimpleTestCase
from django.urls import resolve, reverse
from apps.showroom.views import (
    CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView
)


class URLTests(SimpleTestCase):
    def test_list_url(self):
        url = reverse("showroom:car_list")
        self.assertEqual(resolve(url).func.view_class, CarListView)

    def test_detail_url(self):
        url = reverse("showroom:car_detail", kwargs={
                      "slug": "ford-focus-2020"})
        self.assertEqual(resolve(url).func.view_class, CarDetailView)

    def test_create_url(self):
        url = reverse("showroom:car_create")
        self.assertEqual(resolve(url).func.view_class, CarCreateView)

    def test_update_url(self):
        url = reverse("showroom:car_edit", kwargs={"slug": "any-slug"})
        self.assertEqual(resolve(url).func.view_class, CarUpdateView)

    def test_delete_url(self):
        url = reverse("showroom:car_delete", kwargs={"slug": "any-slug"})
        self.assertEqual(resolve(url).func.view_class, CarDeleteView)
