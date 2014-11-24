from django.db import models
from django.contrib.auth.models import User


class PartnerGroup(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Download(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='downloads')
    partner_group = models.ForeignKey(PartnerGroup, blank=False, null=False)

class Partner(models.Model):
    user = models.OneToOneField(User)
    group = models.ForeignKey(PartnerGroup, blank=False, null=False)

    def __unicode__(self):
        return "{0} ({1})".format(self.user.username, self.group)
