from django.urls import path
from django.http import HttpResponse

app_name = "showroom"

def placeholder(request):
    return HttpResponse("🚗 Showroom app placeholder")

urlpatterns = [
    path("", placeholder, name="index"),
]
