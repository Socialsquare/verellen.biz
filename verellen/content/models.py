from django.db import models
from tinymce.models import HTMLField

class FooterContent(models.Model):
    contact_header = models.CharField(max_length=200)
    contact_body = HTMLField()

    social_header = models.CharField(max_length=200)
    social_body = HTMLField()

    newsletter_header = models.CharField(max_length=200)

    def __unicode__(self):
        return 'Footer content'

class AboutContent(models.Model):
    header = models.CharField(max_length=200)
    body = HTMLField()

    def __unicode__(self):
        return 'About content'

class HomeContent(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return 'Home content'
