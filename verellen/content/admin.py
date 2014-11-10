from django.contrib import admin
from content.models import FooterContent, AboutContent, HomeContent

class FooterContentAdmin(admin.ModelAdmin):
    fields = [
        'contact_header',
        'contact_body',
        'social_header',
        'social_body',
        'newsletter_header',
    ]

class AboutContentAdmin(admin.ModelAdmin):
    fields = [ 'header', 'body' ]

class HomeContentAdmin(admin.ModelAdmin):
    fields = [ 'title' ]

admin.site.register(FooterContent, FooterContentAdmin)
admin.site.register(AboutContent, AboutContentAdmin)
admin.site.register(HomeContent, HomeContentAdmin)
