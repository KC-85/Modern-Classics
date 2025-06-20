# apps/delivery/views.py

from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import DeliveryOption, OrderDelivery

# Decorator shortcut
login_dispatch = method_decorator(login_required, name='dispatch')


@login_dispatch
class DeliveryOptionListView(ListView):
    model = DeliveryOption
    template_name = "delivery/option_list.html"
    context_object_name = "options"
    paginate_by = 20  # if you want pagination


@login_dispatch
class DeliveryOptionCreateView(CreateView):
    model = DeliveryOption
    fields = ['name', 'price', 'description']  # adjust to your model
    template_name = "delivery/option_form.html"
    success_url = reverse_lazy("delivery:option_list")


@login_dispatch
class DeliveryOptionUpdateView(UpdateView):
    model = DeliveryOption
    fields = ['name', 'price', 'description']
    template_name = "delivery/option_form.html"
    success_url = reverse_lazy("delivery:option_list")


@login_dispatch
class DeliveryOptionDeleteView(DeleteView):
    model = DeliveryOption
    template_name = "delivery/option_confirm_delete.html"
    success_url = reverse_lazy("delivery:option_list")


@login_dispatch
class OrderDeliveryUpdateView(UpdateView):
    """
    Allows a user to select/change the delivery option 
    for a given OrderDelivery instance.
    """
    model = OrderDelivery
    fields = ['delivery_option']
    template_name = "delivery/orderdelivery_form.html"
    success_url = reverse_lazy("orders:success")
