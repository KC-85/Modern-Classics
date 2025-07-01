# core/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Allauth (accounts)
    path("accounts/", include("allauth.urls")),

    # Home → redirect to showroom list
    path(
        "",
        RedirectView.as_view(pattern_name="showroom:car_list", permanent=False),
        name="home",
    ),

    # Showroom (cars browsing & CRUD)
    path(
        "showroom/",
        include(("apps.showroom.urls", "showroom"), namespace="showroom"),
    ),

    # User profiles, etc.
    path("users/", include("apps.users.urls")),

    # Orders & checkout
    path("orders/", include("apps.orders.urls")),

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
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
