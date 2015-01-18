from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from partner.models import Partner, PartnerGroup, TearSheet, PriceList, SalesTool

class UserInline(admin.TabularInline):
    model = User

class PartnerGroupAdmin(admin.ModelAdmin):
    fields = [ 'name' ]

class PartnerInline(admin.TabularInline):
    model = Partner
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (PartnerInline,)
    list_display = UserAdmin.list_display + ('list_display_partner',)

    def list_display_partner(self, user):
        if user.partner:
            return user.partner.group.name
        else:
            return None

    list_display_partner.short_description = "Partner group"

class PriceListAdmin(admin.ModelAdmin):
    fields = [ 'name', 'file', 'partner_group' ]
    list_display = [ 'name', 'partner_group' ]

class TearSheetAdmin(admin.ModelAdmin):
    fields = [ 'category', 'name', 'file', 'image_file' ]
    list_display = [ 'name', 'category' ]

class SalesToolAdmin(admin.ModelAdmin):
    fields = [ 'name', 'file' ]
    list_display = [ 'name', 'file' ]
    list_editable = [ 'file' ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(PartnerGroup, PartnerGroupAdmin)

admin.site.register(TearSheet, TearSheetAdmin)
admin.site.register(PriceList, PriceListAdmin)
admin.site.register(SalesTool, SalesToolAdmin)
