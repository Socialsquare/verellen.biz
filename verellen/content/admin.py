from django.contrib import admin
from content.models import ProductContent, FooterContent, AboutContent, HomeContent, MenuContent, CarouselImage

class ProductContentAdmin(admin.ModelAdmin):
    fields = [ 'product_body' ]

class FooterContentAdmin(admin.ModelAdmin):
    fields = [
        'contact_header_left',
        'contact_header_middle',
        'contact_header_right',
        'contact_body_left',
        'contact_body_middle',
        'contact_body_right',
        'social_header',
        'social_body',
        'newsletter_header',
    ]

class MenuContentAdmin(admin.ModelAdmin):
    fields = [
        'products_label',
        'about_label',
        'retailers_label',
        'partner_label',
        'login_label',
    ]

class AboutContentAdmin(admin.ModelAdmin):
    fields = [ 'body' ]

class CarouselImageInline(admin.TabularInline):
    model = CarouselImage
    fields = [ 'image_file', 'title', 'product' ]

class HomeContentAdmin(admin.ModelAdmin):
    fields = [ 'title', ]
    inlines = [ CarouselImageInline, ]

admin.site.register(ProductContent, ProductContentAdmin)
admin.site.register(FooterContent, FooterContentAdmin)
admin.site.register(AboutContent, AboutContentAdmin)
admin.site.register(HomeContent, HomeContentAdmin)
admin.site.register(MenuContent, MenuContentAdmin)
