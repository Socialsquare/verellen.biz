from django.db import models
from tinymce.models import HTMLField

class Image(models.Model):
    image_file = models.ImageField(upload_to='products')
    description = models.TextField(null=True)

    def __unicode__(self):
        if self.description:
            return self.description
        else:
            return unicode(self.image_file)

class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = HTMLField()
    dimensions = HTMLField()

    images = models.ManyToManyField(Image)

    # TODO: mark this from the admin
    @property
    def main_image(self):
        return self.images.first()

    def __unicode__(self):
        return self.name
