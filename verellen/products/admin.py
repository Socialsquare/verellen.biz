from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from products.models import Product, Image, Category

class CategoryInline(admin.TabularInline):
    model = Category

class ImageInline(AdminImageMixin, admin.TabularInline):
    model = Image

class ProductAdmin(admin.ModelAdmin):
    fields = [ 'name', 'category', 'description', 'dimensions' ]
    inlines = [ ImageInline ]

    list_display = [ 'name', 'category', 'number_of_images' ]
    list_editable = [ 'category' ]

class CategoryAdmin(admin.ModelAdmin):
    fields = [ 'name' ]

    list_display = [ 'name', 'slug' ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
