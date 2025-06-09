from django.urls import path
from django.http import HttpResponse

app_name = "common"

def placeholder(request):
    return HttpResponse("🔧 Common app placeholder")

urlpatterns = [
    path("", placeholder, name="index"),
]
