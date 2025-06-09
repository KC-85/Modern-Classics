from django.urls import path
from django.http import HttpResponse

app_name = "users"

def placeholder(request):
    return HttpResponse("👤 Users app placeholder")

urlpatterns = [
    path("", placeholder, name="index"),
]
