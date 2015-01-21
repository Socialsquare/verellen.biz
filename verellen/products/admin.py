from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from products.models import Product, Image, Category
from products.forms import ProductAdminForm

class CategoryInline(admin.TabularInline):
    model = Category

class ImageInline(AdminImageMixin, admin.TabularInline):
    model = Image

class ProductInline(admin.TabularInline):
    model = Product

class ProductAdmin(admin.ModelAdmin):
    fields = [ 'name', 'featured', 'tearsheet', 'category', 'description', 'dimensions', 'main_image' ]
    inlines = [ ImageInline ]

    list_display = [ 'name', 'featured', 'category', 'tearsheet', 'number_of_images', 'main_image', 'admin_thumbnail' ]
    list_editable = [ 'category', 'featured' ]

    form = ProductAdminForm

class CategoryAdmin(admin.ModelAdmin):
    fields = [ 'name', 'image' ]
    list_display = [ 'name', 'slug', 'order', 'image']
    list_editable = ['order']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
