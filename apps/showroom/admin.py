from django.contrib import admin
from .models import CarMake, CarModel, Car

@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "make")
    list_filter  = ("make",)
    search_fields = ("name",)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display   = ("__str__", "year", "price", "condition")
    list_filter    = ("condition", "year", "make")
    search_fields  = ("make__name", "model__name", "specifications")
    prepopulated_fields = {"slug": ("make", "model", "year")}
    readonly_fields = ("created_at", "updated_at")
