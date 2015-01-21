from django.contrib import admin
from retailers.models import Retailer

class RetailerAdmin(admin.ModelAdmin):
    fields = ['partner', 'address', 'city', 'state', 'zip_code', 'country', 'phone', 'website']
    list_display = [ 'partner', 'city', 'phone' ]

admin.site.register(Retailer, RetailerAdmin)
