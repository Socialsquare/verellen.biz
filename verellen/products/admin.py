from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from products.models import Product, Image, Category
from products.forms import ProductAdminForm

class CategoryInline(admin.TabularInline):
    model = Category

class ImageInline(AdminImageMixin, admin.TabularInline):
    model = Image
    fields = [ 'position', 'image_file', 'description' ]
    sortable_field_name = 'position'
    extra = 0

class ProductInline(admin.TabularInline):
    model = Product

class ProductAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'featured',
        'category',
        'tearsheet',
        'tearsheet_metric',
        'description',
        'dimensions',
    ]

    inlines = [ ImageInline ]

    list_display = [
        'name',
        'featured',
        'category',
        'number_of_images',
        'admin_thumbnail',
    ]

    list_editable = [ 'featured' ]

    search_fields = [ 'name' ]

    form = ProductAdminForm

class CategoryAdmin(admin.ModelAdmin):
    fields = [ 'name', 'image' ]
    list_display = [ 'name', 'slug', 'order', 'image']
    list_editable = ['order']

    search_fields = [ 'name' ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
