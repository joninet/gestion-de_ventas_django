from django.contrib import admin

from .models import Customer, Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock',)
    list_filter = ('name',)
    search_fields = ('name', 'stock',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'addres',)
    list_filter = ('name',)
    search_fields = ('name',)