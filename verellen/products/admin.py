from django.contrib import admin
from products.models import Product, Image

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'dimensions', 'images']

class ImageAdmin(admin.ModelAdmin):
    fields = ['image_file', 'description']

admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
