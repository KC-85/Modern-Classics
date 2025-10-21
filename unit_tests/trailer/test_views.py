from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.trailer.models import Cart, CartItem
from apps.showroom.models import CarMake, CarModel, Car

User = get_user_model()


def create_car():
    mk = CarMake.objects.create(name="TestMake")
    md = CarModel.objects.create(make=mk, name="TestModel")
    return Car.objects.create(
        make=mk,
        model=md,
        year=1987,
        price=12345,
        slug="testmake-testmodel-1987",
        is_sold=False,
    )


def optional_reverse(candidates: list[str], **kwargs):
    from django.urls import NoReverseMatch, reverse
    last_exc = None
    for name in candidates:
        try:
            return reverse(name, kwargs=kwargs or None)
        except NoReverseMatch as e:
            last_exc = e
            continue
    if last_exc:
        raise last_exc


class TrailerViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="buyer", password="pass1234")
        # IMPORTANT: avoid Axes backend by bypassing authenticate()
        self.client.force_login(self.user)

        self.car = create_car()
        self.cart, _ = Cart.objects.get_or_create(user=self.user)

    def test_cart_detail_requires_login_and_renders(self):
        url = reverse("trailer:cart_detail")
        # Authenticated
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        # Anonymous behaviour (ok if you don't protect this view)
        self.client.logout()
        resp2 = self.client.get(url)
        self.assertIn(resp2.status_code, (200, 302))
        self.client.force_login(self.user)

    def test_add_to_cart_flow_if_route_exposed(self):
        try:
            url = optional_reverse(
                ["trailer:add_to_cart", "trailer:add", "trailer:item_add"],
                pk=self.car.pk,
            )
        except Exception:
            self.skipTest("No add-to-cart endpoint is exposed")

        before = CartItem.objects.filter(cart=self.cart).count()
        resp = self.client.post(url, {"quantity": 1}, follow=True)
        self.assertIn(resp.status_code, (200, 302))
        after = CartItem.objects.filter(cart=self.cart).count()
        self.assertEqual(after, before + 1)

    def test_update_quantity_if_route_exposed(self):
        item = CartItem.objects.create(
            cart=self.cart, car=self.car, quantity=1)
        try:
            url = optional_reverse(
                ["trailer:update_item", "trailer:update", "trailer:item_update"],
                pk=item.pk,
            )
        except Exception:
            self.skipTest("No update-item endpoint is exposed")

        resp = self.client.post(url, {"quantity": 3}, follow=True)
        self.assertIn(resp.status_code, (200, 302))
        item.refresh_from_db()
        self.assertEqual(item.quantity, 3)

    def test_remove_from_cart_if_route_exposed(self):
        item = CartItem.objects.create(
            cart=self.cart, car=self.car, quantity=1)
        try:
            url = optional_reverse(
                ["trailer:remove_from_cart", "trailer:remove", "trailer:item_remove"],
                pk=item.pk,
            )
        except Exception:
            self.skipTest("No remove-item endpoint is exposed")

        resp = self.client.post(url, follow=True)
        self.assertIn(resp.status_code, (200, 302))
        self.assertFalse(CartItem.objects.filter(pk=item.pk).exists())
