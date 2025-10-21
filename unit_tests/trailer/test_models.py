from django.contrib.auth import get_user_model
from django.test import TestCase
from apps.trailer.models import Cart, CartItem

from apps.showroom.models import CarMake, CarModel, Car


User = get_user_model()


def make_car(idx=1, price=10000):
    make = CarMake.objects.create(name=f"Make{idx}")
    model = CarModel.objects.create(make=make, name=f"Model{idx}")
    car = Car.objects.create(
        make=make,
        model=model,
        year=1990 + idx,
        price=price,
        slug=f"make{idx}-model{idx}-{1990+idx}",
        is_sold=False,
    )
    return car


class TrailerModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="buyer", password="pass1234")
        self.cart = Cart.objects.create(user=self.user)

    def test_cart_str(self):
        s = str(self.cart)
        self.assertTrue(self.user.username in s or "Cart" in s)

    def test_cartitem_relationships(self):
        car = make_car(1)
        item = CartItem.objects.create(cart=self.cart, car=car, quantity=2)
        self.assertEqual(item.cart, self.cart)
        self.assertEqual(item.car, car)
        self.assertEqual(item.quantity, 2)

    def test_multiple_items_possible(self):
        car1 = make_car(1, 10000)
        car2 = make_car(2, 20000)
        CartItem.objects.create(cart=self.cart, car=car1, quantity=1)
        CartItem.objects.create(cart=self.cart, car=car2, quantity=1)
        self.assertEqual(CartItem.objects.filter(cart=self.cart).count(), 2)
