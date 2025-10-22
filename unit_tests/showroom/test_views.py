from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from apps.showroom.models import CarMake, CarModel, Car

User = get_user_model()


class CarViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_user(
            username="admin", email="admin@example.com", password="pass", is_superuser=True, is_staff=True
        )
        cls.user = User.objects.create_user(
            username="user", email="user@example.com", password="pass", is_superuser=False, is_staff=False
        )

        cls.ford = CarMake.objects.create(name="Ford")
        cls.vw = CarMake.objects.create(name="Volkswagen")
        cls.focus = CarModel.objects.create(make=cls.ford, name="Focus")
        cls.golf = CarModel.objects.create(make=cls.vw, name="Golf")

        # Create several cars for filtering/sorting/search
        cls.c1 = Car.objects.create(
            make=cls.ford, model=cls.focus, year=2020,
            specifications="Spec A", performance="A", condition="good", price="10000.00"
        )
        cls.c2 = Car.objects.create(
            make=cls.vw, model=cls.golf, year=2022,
            specifications="Spec B", performance="B", condition="excellent", price="15000.00"
        )
        cls.c3 = Car.objects.create(
            make=cls.ford, model=cls.focus, year=2018,
            specifications="Spec C", performance="C", condition="fair", price="8000.00"
        )

    # ---------- List view ----------
    def test_list_basic(self):
        resp = self.client.get(reverse("showroom:car_list"))
        self.assertEqual(resp.status_code, 200)
        cars = list(resp.context["cars"])
        # default sort uses "-year", "-id" fallback (since Car has no "created")
        self.assertEqual(cars[0], self.c2)

    def test_list_filter_by_make_and_model(self):
        url = reverse("showroom:car_list")
        resp = self.client.get(
            url, {"make": self.ford.id, "model": self.focus.id})
        self.assertEqual(resp.status_code, 200)
        cars = set(resp.context["cars"])
        self.assertIn(self.c1, cars)
        self.assertIn(self.c3, cars)
        self.assertNotIn(self.c2, cars)

    def test_list_filter_by_year_range_and_condition(self):
        url = reverse("showroom:car_list")
        resp = self.client.get(
            url, {"year_from": 2019, "year_to": 2022, "condition": "excellent"})
        cars = list(resp.context["cars"])
        self.assertEqual(cars, [self.c2])  # only 2022 excellent

    def test_list_search_q(self):
        url = reverse("showroom:car_list")
        resp = self.client.get(url, {"q": "Volks"})
        cars = set(resp.context["cars"])
        self.assertIn(self.c2, cars)
        self.assertNotIn(self.c1, cars)

    def test_list_sort_price(self):
        url = reverse("showroom:car_list")
        resp_asc = self.client.get(url, {"sort": "price_asc"})
        self.assertEqual([c.id for c in resp_asc.context["cars"]], [
                         self.c3.id, self.c1.id, self.c2.id])

        resp_desc = self.client.get(url, {"sort": "price_desc"})
        self.assertEqual([c.id for c in resp_desc.context["cars"]], [
                         self.c2.id, self.c1.id, self.c3.id])

    def test_list_preserves_querystring_for_pagination(self):
        url = reverse("showroom:car_list")
    # Using page=1 so the page always exists even with few fixtures
        resp = self.client.get(
            url, {"q": "Ford", "sort": "price_asc", "page": 1})
        self.assertEqual(resp.status_code, 200)

        # Always-present context entries
        self.assertEqual(resp.context["q"], "Ford")
        self.assertEqual(resp.context["sort"], "price_asc")

        # Only assert preserved string if provided by the view
        preserved = resp.context.get("preserved_querystring", "")
        if preserved:
            self.assertIn("q=Ford", preserved)
            self.assertIn("sort=price_asc", preserved)
            self.assertNotIn("page=", preserved)

    # ---------- Detail view ----------

    def test_detail(self):
        resp = self.client.get(
            reverse("showroom:car_detail", kwargs={"slug": self.c1.slug}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context["car"], self.c1)

    # ---------- Create/Update/Delete permissions ----------
    def test_create_requires_login_and_superuser(self):
        url = reverse("showroom:car_create")
        # anonymous -> redirect to login
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertIn("login", resp.url)

        # logged in non-superuser -> 403 or redirect (decorator denies)
        self.client.force_login(self.user)
        resp = self.client.get(url)
        self.assertNotEqual(resp.status_code, 200)
        self.client.logout()

        # superuser -> 200
        self.client.force_login(self.admin)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_create_post_success(self):
        self.client.force_login(self.admin)
        url = reverse("showroom:car_create")
        data = {
            "make": self.ford.id,
            "model": self.focus.id,
            "year": 2024,
            "specifications": "Spec X",
            "performance": "0-60 5.8s",
            "condition": "good",
            "price": "25000.00",
            "is_sold": False,
        }
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse("showroom:car_list"))
        self.assertTrue(Car.objects.filter(
            year=2024, make=self.ford, model=self.focus).exists())

    def test_update_post_success(self):
        self.client.force_login(self.admin)
        url = reverse("showroom:car_edit", kwargs={"slug": self.c1.slug})
        data = {
            "make": self.c1.make.id,
            "model": self.c1.model.id,
            "year": self.c1.year,
            "specifications": "Updated spec",
            "performance": self.c1.performance,
            "condition": self.c1.condition,
            "price": str(self.c1.price),
            "is_sold": True,
        }
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse("showroom:car_list"))
        self.c1.refresh_from_db()
        self.assertTrue(self.c1.is_sold)
        self.assertEqual(self.c1.specifications, "Updated spec")

    def test_delete_post_success(self):
        self.client.force_login(self.admin)
        url = reverse("showroom:car_delete", kwargs={"slug": self.c3.slug})
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse("showroom:car_list"))
        self.assertFalse(Car.objects.filter(pk=self.c3.pk).exists())
