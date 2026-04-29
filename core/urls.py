# core/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import HomeView

from apps.common.views import robots_txt

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Allauth (accounts)
    path("accounts/", include("allauth.urls")),

    # Hero page
    path("", HomeView.as_view(), name="home"),

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
    path("robots.txt", robots_txt, name="robots_txt"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
