from django.db import models
from django.contrib.auth.models import User

from sorl import thumbnail

from products.models import Category

class PartnerGroup(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Download(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='downloads')

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True

class SalesTool(Download):
    pass

class PriceList(Download):
    partner_group = models.ForeignKey(PartnerGroup, blank=True, null=True)

    def __unicode__(self):
        return '{0} ({1})'.format(self.name, self.partner_group)

class Partner(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=255)
    group = models.ForeignKey(PartnerGroup, blank=False, null=False)

    def __unicode__(self):
        return '{0} ({1})'.format(self.name, self.user.username)
