# apps/showroom/views.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView,
)
from .models import Car
from .forms import CarForm, CarFilterForm

# Only superusers can do create/update/delete
superuser_required = user_passes_test(lambda u: u.is_superuser)

@method_decorator(login_required, name="dispatch")
class CarListView(ListView):
    model               = Car
    template_name       = "showroom/list.html"
    context_object_name = "cars"
    paginate_by         = 10  # <-- pagination here

    def get_queryset(self):
        qs   = super().get_queryset()
        form = CarFilterForm(self.request.GET)
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
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["filter_form"] = CarFilterForm(self.request.GET)
        return ctx

@method_decorator(login_required, name="dispatch")
class CarDetailView(DetailView):
    model         = Car
    template_name = "showroom/detail.html"

@method_decorator([login_required, superuser_required], name="dispatch")
class CarCreateView(CreateView):
    model         = Car
    form_class    = CarForm
    template_name = "showroom/car_form.html"
    success_url   = reverse_lazy("showroom:car_list")

@method_decorator([login_required, superuser_required], name="dispatch")
class CarUpdateView(UpdateView):
    model         = Car
    form_class    = CarForm
    template_name = "showroom/car_form.html"
    success_url   = reverse_lazy("showroom:car_list")

@method_decorator([login_required, superuser_required], name="dispatch")
class CarDeleteView(DeleteView):
    model         = Car
    template_name = "showroom/car_confirm_delete.html"
    success_url   = reverse_lazy("showroom:car_list")
