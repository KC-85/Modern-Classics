# apps/showroom/views.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from urllib.parse import urlencode
from django.db.models import Q
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView,
)
from .models import Car
from .forms import CarForm, CarFilterForm

# Only superusers can do create/update/delete
superuser_required = user_passes_test(lambda u: u.is_superuser)


class CarListView(ListView):
    model = Car
    template_name = "showroom/list.html"
    context_object_name = "cars"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().select_related("make", "model")
        form = CarFilterForm(self.request.GET)

        # ----- structured filters (your existing form) -----
        if form.is_valid():
            data = form.cleaned_data
            if data.get("make"):
                qs = qs.filter(make=data["make"])
            if data.get("model"):
                qs = qs.filter(model=data["model"])
            if data.get("year_from"):
                qs = qs.filter(year__gte=data["year_from"])
            if data.get("year_to"):
                qs = qs.filter(year__lte=data["year_to"])
            if data.get("condition"):
                qs = qs.filter(condition=data["condition"])

        # ----- free-text search (q) -----
        q = (self.request.GET.get("q") or "").strip()
        if q:
            qs = qs.filter(
                Q(make__name__icontains=q) |
                Q(model__name__icontains=q) |
                Q(year__icontains=q)
            )

        # ----- sorting -----
        sort = (self.request.GET.get("sort") or "new").lower()
        if sort == "price_asc":
            qs = qs.order_by("price", "-id")
        elif sort == "price_desc":
            qs = qs.order_by("-price", "-id")
        else:  # "new"
            if hasattr(Car, "created"):           # prefer a created timestamp if you have one
                qs = qs.order_by("-created", "-id")
            else:
                # fallback: newest year first, then newest id
                qs = qs.order_by("-year", "-id")

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        q = (self.request.GET.get("q") or "").strip()
        sort = (self.request.GET.get("sort") or "new").lower()

        # Preserve filters across pagination links
        preserved = self.request.GET.copy()
        if "page" in preserved:
            preserved.pop("page")
        ctx.update({
            "filter_form": CarFilterForm(self.request.GET),
            "q": q,
            "sort": sort,
            "preserved_querystring": urlencode(preserved, doseq=True),
        })
        return ctx


class CarDetailView(DetailView):
    model = Car
    template_name = "showroom/detail.html"


@method_decorator([login_required, superuser_required], name="dispatch")
class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "showroom/car_form.html"
    success_url = reverse_lazy("showroom:car_list")


@method_decorator([login_required, superuser_required], name="dispatch")
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = "showroom/car_form.html"
    success_url = reverse_lazy("showroom:car_list")


@method_decorator([login_required, superuser_required], name="dispatch")
class CarDeleteView(DeleteView):
    model = Car
    template_name = "showroom/car_confirm_delete.html"
    success_url = reverse_lazy("showroom:car_list")
