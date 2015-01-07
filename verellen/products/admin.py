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
    fields = [ 'name', 'category', 'description', 'dimensions', 'main_image' ]
    inlines = [ ImageInline ]

    list_display = [ 'admin_thumbnail', 'name', 'category', 'number_of_images', 'main_image' ]
    list_editable = [ 'category' ]

    form = ProductAdminForm

class CategoryAdmin(admin.ModelAdmin):
    fields = [ 'name' ]
    list_display = [ 'name', 'slug' ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
