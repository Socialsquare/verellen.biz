from django.db import models

class Image(models.Model):
    image_file = models.ImageField(upload_to='media/')
    description = models.TextField(null=True)

    def __unicode__(self):
        return unicode(self.image_file)

class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField(default = 0)

    images = models.ManyToManyField(Image)

    def __unicode__(self):
        return self.name
