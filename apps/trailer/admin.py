from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ("car", "quantity")
    can_delete = False

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created")
    list_filter = ("created", "user")
    search_fields = ("user__username",)
    inlines = [CartItemInline]

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "car", "quantity")
    list_filter = ("cart",)
    search_fields = ("cart__user__username", "car__make__name", "car__model__name")
