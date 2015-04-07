from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from partner.models import Partner, PartnerGroup, PriceList, SalesTool

class UserInline(admin.TabularInline):
    model = User

class PartnerGroupAdmin(admin.ModelAdmin):
    fields = [ 'name' ]

class PartnerInline(admin.TabularInline):
    model = Partner
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (PartnerInline,)
    list_display = UserAdmin.list_display + ('list_display_partner',) + ('display_boutique',)

    def list_display_partner(self, user):
        if user.partner and user.partner.group:
            return user.partner.group.name
        else:
            return None

    def display_boutique(self, user):
        return user.partner and user.partner.is_boutique

    display_boutique.boolean = True

    list_display_partner.short_description = "Partner group"

class PriceListAdmin(admin.ModelAdmin):
    fields = [ 'name', 'file', 'partner_group' ]
    list_display = [ 'name', 'partner_group' ]

class SalesToolAdmin(admin.ModelAdmin):
    fields = [ 'name', 'file', 'is_eu_format' ]
    list_display = [ 'name', 'file', 'is_eu_format' ]
    list_editable = [ 'file', 'is_eu_format' ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(PartnerGroup, PartnerGroupAdmin)

admin.site.register(PriceList, PriceListAdmin)
admin.site.register(SalesTool, SalesToolAdmin)
