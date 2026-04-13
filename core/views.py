from django.views.generic import TemplateView
from django.shortcuts import redirect
from apps.showroom.models import Car

class HomeView(TemplateView):
    template_name = "home/hero.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("showroom:car_list")
        return super().dispatch(request, *args, **kwargs)

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
