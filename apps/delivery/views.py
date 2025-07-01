# apps/delivery/views.py

import math
from django.urls                 import reverse_lazy
from django.views.generic        import ListView, CreateView, UpdateView, DeleteView
from django.views                import View
from django.shortcuts            import get_object_or_404, render, redirect
from django.contrib.auth.mixins  import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators     import method_decorator

from .models   import DeliveryOption
from .forms    import DeliveryDistanceForm
from apps.orders.models import Order

# Decorator shortcut for function-based mixins
login_dispatch = method_decorator(login_required, name='dispatch')

@login_dispatch
class DeliveryOptionListView(ListView):
    model               = DeliveryOption
    template_name       = "delivery/option_list.html"
    context_object_name = "options"
    paginate_by         = 20  # optional

@login_dispatch
class DeliveryOptionCreateView(CreateView):
    model         = DeliveryOption
    fields        = ['name', 'price', 'description']
    template_name = "delivery/option_form.html"
    success_url   = reverse_lazy("delivery:option_list")

@login_dispatch
class DeliveryOptionUpdateView(UpdateView):
    model         = DeliveryOption
    fields        = ['name', 'price', 'description']
    template_name = "delivery/option_form.html"
    success_url   = reverse_lazy("delivery:option_list")

@login_dispatch
class DeliveryOptionDeleteView(DeleteView):
    model         = DeliveryOption
    template_name = "delivery/option_confirm_delete.html"
    success_url   = reverse_lazy("delivery:option_list")


class OrderDeliveryUpdateView(LoginRequiredMixin, View):
    """
    Distance-based delivery: lets the user enter miles,
    calculates fee in the Order model, and redirects back.
    """
    template_name = "delivery/orderdelivery_form.html"

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk, user=request.user)
        form = DeliveryDistanceForm(initial={
            "delivery_distance": order.delivery_distance
        })
        return render(request, self.template_name, {
            "form": form, "order": order
        })

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk, user=request.user)
        form = DeliveryDistanceForm(request.POST)
        if form.is_valid():
            order.delivery_distance = form.cleaned_data["delivery_distance"]
            order.save(update_fields=["delivery_distance"])
            return redirect("orders:detail", order.pk)
        return render(request, self.template_name, {
            "form": form, "order": order
        })
