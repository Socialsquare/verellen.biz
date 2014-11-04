from django.contrib import admin
from retailers.models import Retailer

class RetailerAdmin(admin.ModelAdmin):
    field = ['name', 'address']

admin.site.register(Retailer, RetailerAdmin)
