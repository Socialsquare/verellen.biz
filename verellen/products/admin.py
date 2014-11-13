from django.contrib import admin
from products.models import Product, Image

class ImageInline(admin.TabularInline):
    model = Image

class ProductAdmin(admin.ModelAdmin):
    fields = [ 'name', 'description', 'dimensions' ]
    inlines = (ImageInline,)

admin.site.register(Product, ProductAdmin)
