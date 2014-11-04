from django.contrib import admin
from content.models import FooterContent

class FooterContentAdmin(admin.ModelAdmin):
    fields = [
        'contact_header',
        'contact_body',
        'social_header',
        'social_body',
        'newsletter_header',
    ]

admin.site.register(FooterContent, FooterContentAdmin)
