from django.db import models
from django.forms import ModelChoiceField
from django.template.defaultfilters import slugify

from tinymce.models import HTMLField
from sorl import thumbnail
from sorl.thumbnail import get_thumbnail


class Category(models.Model):
    image = thumbnail.ImageField(upload_to='categories', default='default_image')
    name = models.CharField(max_length = 200)
    slug = models.SlugField(unique = True)
    order = models.IntegerField('Position', default=0)

    def save(self, *args, **kwargs):
        if not self.id or not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Product(models.Model):
    name = models.CharField(max_length = 200)
    tearsheet = models.FileField(upload_to="product_tear_sheets", default="no_image.png")
    featured = models.BooleanField(default=False)
    description = HTMLField(blank=True, default="")
    dimensions = HTMLField(blank=True, default="")
    main_image = models.ForeignKey('Image', related_name='+', blank=True, null=True)
    category = models.ForeignKey(Category)

    def get_main_image(self):
        if not self.main_image is None:
            return self.main_image
        else:
            return self.image_set.first()

    def number_of_images(self):
        return self.image_set.all().count()

    def admin_thumbnail(self):
        img = self.get_main_image()
        if img:
            t = get_thumbnail(img.image_file, '70x70', crop='center', quality=99)
            return u'<img src="%s"/>' % (t.url)
        else:
            return u'<img src=""/>'
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True

    def __unicode__(self):
        return self.name

class Image(models.Model):
    image_file = thumbnail.ImageField(upload_to='products')
    product = models.ForeignKey(Product)
    description = models.TextField(null=True, blank=True)

    def image_tag(self):
        return u'<img width="110" height="110" src="%s" />' % self.image_file.url
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __unicode__(self):
        if self.description:
            return self.description
        else:
            return unicode(self.image_file)
