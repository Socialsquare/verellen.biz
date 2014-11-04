from django.contrib import admin
from products.models import Product

class ProductAdmin(admin.ModelAdmin):
    field = ['name', 'price']

admin.site.register(Product, ProductAdmin)
