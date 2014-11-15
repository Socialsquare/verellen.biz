from django.contrib import admin
from content.models import FooterContent, AboutContent, HomeContent, MenuContent

class FooterContentAdmin(admin.ModelAdmin):
    fields = [
        'contact_header',
        'contact_body',
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

class HomeContentAdmin(admin.ModelAdmin):
    fields = [ 'title' ]

admin.site.register(FooterContent, FooterContentAdmin)
admin.site.register(AboutContent, AboutContentAdmin)
admin.site.register(HomeContent, HomeContentAdmin)
admin.site.register(MenuContent, MenuContentAdmin)
