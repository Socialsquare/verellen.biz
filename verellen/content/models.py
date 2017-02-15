from django.db import models

from tinymce.models import HTMLField
from sorl import thumbnail

from products.models import Product


class ProductContent(models.Model):
    product_body = HTMLField(default='')

    def __unicode__(self):
        return 'Product content'


class FooterContent(models.Model):
    contact_header_left = models.CharField(max_length=200)
    contact_header_middle = models.CharField(max_length=200)
    contact_header_right = models.CharField(max_length=200)
    contact_body_left = HTMLField()
    contact_body_middle = HTMLField()
    contact_body_right = HTMLField()

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


class ContractContent(models.Model):
    header = models.CharField(max_length=200)
    body = HTMLField()

    def __unicode__(self):
        return 'Contract content'


class CarouselImage(models.Model):
    image_file = thumbnail.ImageField(upload_to='carousel')
    title = models.CharField(max_length=200, blank=True, null=True)
    product = models.ForeignKey(Product, blank=True, null=True)
    home_content = models.ForeignKey(HomeContent)


class MenuContent(models.Model):
    products_label = models.CharField(max_length=200)
    about_label = models.CharField(max_length=200)
    retailers_label = models.CharField(max_length=200)
    partner_label = models.CharField(max_length=200)
    login_label = models.CharField(max_length=200)
    resources_label = models.CharField(max_length=200)
    contract_label = models.CharField(max_length=200)

    def __unicode__(self):
        return 'Menu content'
