# apps/common/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.showroom.models import Car


class CarSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # Only index cars that are for sale (not sold)
        return Car.objects.filter(is_sold=False)

    def lastmod(self, obj: Car):
        return obj.updated_at

    def location(self, obj: Car):
        return obj.get_absolute_url()


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        # List named URL patterns you want indexed
        return [
            "home",                    # your hero page
            "showroom:car_list",       # showroom list
            "common:faq_list",         # FAQ index (adjust if different)
            "common:contact",          # contact page
            "common:newsletter",       # newsletter signup
        ]

    def location(self, name):
        return reverse(name)
