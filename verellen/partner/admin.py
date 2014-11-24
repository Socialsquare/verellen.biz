from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from partner.models import Partner, PartnerType

class UserInline(admin.TabularInline):
    model = User

class PartnerTypeAdmin(admin.ModelAdmin):
    fields = [ 'name' ]

class PartnerInline(admin.TabularInline):
    model = Partner
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (PartnerInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(PartnerType, PartnerTypeAdmin)
