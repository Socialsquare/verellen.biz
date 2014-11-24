from django.db import models
from django.contrib.auth.models import User

class PartnerType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Partner(models.Model):
    user = models.OneToOneField(User)
    partner_type = models.ForeignKey(PartnerType, blank=False, null=False)

    def __unicode__(self):
        return "{0} ({1})".format(self.user.username, self.partner_type)
