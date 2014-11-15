from django.db import models
from tinymce.models import HTMLField

from sorl import thumbnail
from thumbnail.models import AsyncThumbnailMixin
#AsyncThumbnailMixin,

class Category(models.Model):
    name = models.CharField(max_length = 200);

    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = HTMLField()
    dimensions = HTMLField()

    category = models.ForeignKey(Category)

    # TODO: mark this from the admin
    @property
    def main_image(self):
        return self.image_set.first()

    def __unicode__(self):
        return self.name

class Image(models.Model):
    #image_field_name = 'image_file'
    image_file = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product)
    description = models.TextField(null=True)

    def __unicode__(self):
        if self.description:
            return self.description
        else:
            return unicode(self.image_file)
