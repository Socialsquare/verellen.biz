from django.contrib import admin
from products.models import Product, Image

class ProductAdmin(admin.ModelAdmin):
    field = ['name', 'price']

class ImageAdmin(admin.ModelAdmin):
    field = ['name', 'price']

admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
