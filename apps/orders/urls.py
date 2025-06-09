from django.urls import path
from django.http import HttpResponse

app_name = "orders"

def placeholder(request):
    return HttpResponse("📦 Orders app placeholder")

urlpatterns = [
    path("", placeholder, name="index"),
]
