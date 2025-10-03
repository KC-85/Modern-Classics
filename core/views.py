from django.views.generic import TemplateView
from apps.showroom.models import Car

class HomeView(TemplateView):
    template_name = "home/hero.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = (
            Car.objects
               .filter(is_sold=False)
               .exclude(image="placeholder")      # ← key line
               .order_by("-created_at")
        )
        ctx["featured_cars"] = qs[:10]
        return ctx
