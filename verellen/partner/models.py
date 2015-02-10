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
    is_eu_format = models.BooleanField(default=False,
                                       verbose_name="Is EU format")

class PriceList(Download):
    partner_group = models.ForeignKey(PartnerGroup, blank=True, null=True)

    def __unicode__(self):
        return '{0} ({1})'.format(self.name, self.partner_group)

class Partner(models.Model):
    user = models.OneToOneField(User)
    expiryDate = models.DateTimeField(null=True, blank=True)
    hide_price = models.BooleanField(default=False)
    show_metric = models.BooleanField(default=False)
    show_eu_price = models.BooleanField(default=False,
                                        verbose_name="Show EU tools")
    name = models.CharField(max_length=255)
    group = models.ForeignKey(PartnerGroup, blank=True, null=True, default=None)

    def __unicode__(self):
        return '{0} ({1})'.format(self.name, self.user.username)
