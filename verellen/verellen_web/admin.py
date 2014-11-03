from django.contrib import admin
from verellen_web.models import Product

class ProductAdmin(admin.ModelAdmin):
    field = ['name', 'price']

admin.site.register(Product, ProductAdmin)
