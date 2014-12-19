from django.contrib import admin
from retailers.models import Retailer

class RetailerAdmin(admin.ModelAdmin):
    fields = ['name', 'address', 'city', 'state', 'zip_code', 'phone', 'website']

admin.site.register(Retailer, RetailerAdmin)
