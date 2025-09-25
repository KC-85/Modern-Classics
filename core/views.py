from django.views.generic import TemplateView
from apps.showroom.models import Car

class HomeView(TemplateView):
    template_name = "home/hero.html"  # template below

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Optional: show unsold, newest cars in the hero carousel
        ctx["featured_cars"] = Car.objects.filter(is_sold=False).order_by("-created_at")[:6]
        return ctx
