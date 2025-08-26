from django.contrib.admin.sites import site
from django.test import TestCase
from common.models import Newsletter, Contact, FAQ

"""
This unit-test is to confirm the functionality of common/admin.py
and to ensure that the database models are registered to the
Django admin panel without any errors.
"""

class AdminSiteTest(TestCase):
    """ Test case for Django Admin Site/Panel """

    def test_newsletter_registered(self):
        """ 
        Test if Newsletter model is registered in Admin 
        """
        self.assertTrue(site.is_registered(Newsletter))

    def test_contact_registered(self):
        """
        Test if Contact model is registered in Admin
        """
        self.assertTrue(site.is_registered(Contact))

    def test_faq_registered(self):
        """
        Test if FAQ model is registered in Admin
        """
        self.assertTrue(site.is_registered(FAQ))
