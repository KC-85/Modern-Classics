from django.test import SimpleTestCase
from django.urls import get_resolver


class DeliveryURLTests(SimpleTestCase):
    def test_namespace_exists(self):
        """
        Ensure the `delivery` namespace is wired into the project.
        """
        resolver = get_resolver()
        namespaces = {ns for (ns, _) in resolver.namespace_dict.items()}
        self.assertIn("delivery", namespaces,
                      "Include('delivery.urls', namespace='delivery') missing?")
