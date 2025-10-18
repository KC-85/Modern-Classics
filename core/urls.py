# core/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import views as sitemap_views

from core.views import HomeView

from apps.common.sitemaps import CarSitemap, StaticViewSitemap
from apps.common.views import robots_txt

sitemaps = {
    "cars":   CarSitemap,
    "static": StaticViewSitemap,
}

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Allauth (accounts)
    path("accounts/", include("allauth.urls")),

    # Hero page
    path("", HomeView.as_view(), name="home"),

    # Home → redirect to showroom list
    path(
        "",
        RedirectView.as_view(
            pattern_name="showroom:car_list", permanent=False),
        name="home",
    ),

    # Showroom (cars browsing & CRUD)
    path(
        "showroom/",
        include(("apps.showroom.urls", "showroom"), namespace="showroom"),
    ),

    # User profiles, etc.
    path("users/", include("apps.users.urls")),

    # Checkout
    path("checkout/", include("apps.checkout.urls")),

    # Common utilities (FAQs, contacts…)
    path("common/", include("apps.common.urls")),

    # Cart / “trailer”
    path("trailer/", include("apps.trailer.urls")),

    # Delivery / shipping
    path(
        "delivery/",
        include(
            ("apps.delivery.urls", "delivery"),
            namespace="delivery"
        ),
    ),

    # SEO
    path("sitemap.xml", sitemap_views.sitemap, {
         "sitemaps": sitemaps}, name="sitemap"),
    path("robots.txt", robots_txt, name="robots_txt"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
