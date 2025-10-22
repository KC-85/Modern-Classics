from django.test import TestCase
from apps.showroom.forms import CarFilterForm, CarForm
from apps.showroom.models import CarMake, CarModel, Car


class CarFilterFormTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.ford = CarMake.objects.create(name="Ford")
        cls.vw = CarMake.objects.create(name="Volkswagen")
        cls.focus = CarModel.objects.create(make=cls.ford, name="Focus")
        cls.golf = CarModel.objects.create(make=cls.vw, name="Golf")

    def test_blank_form_makes_populated_models_empty(self):
        form = CarFilterForm(data={})
        self.assertIn(self.ford, form.fields["make"].queryset)
        self.assertIn(self.vw, form.fields["make"].queryset)
        self.assertEqual(list(form.fields["model"].queryset), [])

    def test_models_filtered_by_make(self):
        form = CarFilterForm(data={"make": str(self.ford.id)})
        qs = form.fields["model"].queryset
        self.assertIn(self.focus, qs)
        self.assertNotIn(self.golf, qs)

    def test_invalid_make_keeps_models_empty(self):
        form = CarFilterForm(data={"make": "999999"})
        self.assertEqual(list(form.fields["model"].queryset), [])

    def test_condition_choices_include_any_plus_model_choices(self):
        form = CarFilterForm()
        expected = [("", "Any")] + list(Car.CONDITION_CHOICES)
        self.assertEqual(form.fields["condition"].choices, expected)

    def test_year_fields_optional_and_valid_blank(self):
        form = CarFilterForm(data={"year_from": "", "year_to": ""})
        self.assertTrue(form.is_valid())

    def test_crispy_helper_config(self):
        form = CarFilterForm()
        self.assertTrue(hasattr(form, "helper"))
        self.assertEqual(form.helper.form_method, "get")


class CarFormTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.make = CarMake.objects.create(name="Ford")
        cls.model = CarModel.objects.create(make=cls.make, name="Focus")

    def test_fields_and_helper(self):
        form = CarForm()
        self.assertTrue(hasattr(form, "helper"))
        self.assertEqual(form.helper.form_method, "post")
        self.assertCountEqual(
            list(form.fields.keys()),
            ["make", "model", "year", "specifications", "performance",
                "condition", "image", "price", "is_sold"]
        )

    def test_valid_data_saves(self):
        data = {
            "make": self.make.id,
            "model": self.model.id,
            "year": 2021,
            "specifications": "Spec sheet",
            "performance": "0-60 6.2s",
            "condition": "good",
            "price": "12345.67",
            "is_sold": False,
        }
        form = CarForm(data=data)
        self.assertTrue(form.is_valid(), form.errors)
        car = form.save()
        self.assertEqual(car.make, self.make)
        self.assertEqual(car.model, self.model)
