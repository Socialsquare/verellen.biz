from django.contrib import admin
from products.models import Product, Image, Category

class CategoryInline(admin.TabularInline):
    model = Category

class ImageInline(admin.TabularInline):
    model = Image

class ProductAdmin(admin.ModelAdmin):
    fields = [ 'name', 'category', 'description', 'dimensions' ]
    inlines = [ImageInline]

    list_display = [ 'name', 'category' ]
    list_editable = [ 'category' ]

class CategoryAdmin(admin.ModelAdmin):
    fields = [ 'name' ]

    list_display = [ 'name', 'slug' ]



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
