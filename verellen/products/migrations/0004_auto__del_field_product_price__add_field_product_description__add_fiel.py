# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Product.price'
        db.delete_column(u'products_product', 'price')

        # Adding field 'Product.description'
        db.add_column(u'products_product', 'description',
                      self.gf('tinymce.models.HTMLField')(default='Dummy description'),
                      keep_default=False)

        # Adding field 'Product.dimensions'
        db.add_column(u'products_product', 'dimensions',
                      self.gf('tinymce.models.HTMLField')(default='Dummy dimensions'),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Product.price'
        db.add_column(u'products_product', 'price',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Product.description'
        db.delete_column(u'products_product', 'description')

        # Deleting field 'Product.dimensions'
        db.delete_column(u'products_product', 'dimensions')


    models = {
        u'products.image': {
            'Meta': {'object_name': 'Image'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'description': ('tinymce.models.HTMLField', [], {}),
            'dimensions': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Image']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['products']