from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ("car", "quantity")
    can_delete = False

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    # Cart has fields: id (PK), user, created_at
    list_display  = ('id', 'user', 'created_at')
    list_filter   = ('created_at', 'user')
    search_fields = ('user__username',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    # CartItem has: cart (FK), car (FK), quantity
    list_display  = ('cart', 'car', 'quantity')
    list_filter   = ('car',)
    search_fields = ('cart__user__username', 'car__make__name', 'car__model__name')
