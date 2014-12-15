from django.contrib import admin
from content.models import FooterContent, AboutContent, HomeContent, MenuContent, CarouselImage

class FooterContentAdmin(admin.ModelAdmin):
    fields = [
        'contact_header',
        'contact_body_left',
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
    fields = [ 'header', 'body' ]

class CarouselImageInline(admin.TabularInline):
    model = CarouselImage
    fields = [ 'image_file', 'title' ]

class HomeContentAdmin(admin.ModelAdmin):
    fields = [ 'title', ]
    inlines = [ CarouselImageInline, ]

admin.site.register(FooterContent, FooterContentAdmin)
admin.site.register(AboutContent, AboutContentAdmin)
admin.site.register(HomeContent, HomeContentAdmin)
admin.site.register(MenuContent, MenuContentAdmin)
