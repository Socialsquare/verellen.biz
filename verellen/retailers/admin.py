from django.contrib import admin
from retailers.models import Retailer#, VerellenBoutiques

class RetailerAdmin(admin.ModelAdmin):
    fields = ['partner', 'address', 'city', 'state', 'zip_code', 'country', 'phone', 'website']
    list_display = [ 'partner', 'city', 'phone' ]

# class VerellenBoutiquesAdmin(admin.ModelAdmin):
#     fields = ['title', 'description']
#     list_display = ['title', 'description']

admin.site.register(Retailer, RetailerAdmin)
# admin.site.register(VerellenBoutiques, VerellenBoutiquesAdmin)