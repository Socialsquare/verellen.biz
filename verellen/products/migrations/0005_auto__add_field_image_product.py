# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Image.product'
        db.add_column(u'products_image', 'product',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['products.Product']),
                      keep_default=False)

        # Removing M2M table for field images on 'Product'
        db.delete_table(db.shorten_name(u'products_product_images'))


    def backwards(self, orm):
        # Deleting field 'Image.product'
        db.delete_column(u'products_image', 'product_id')

        # Adding M2M table for field images on 'Product'
        m2m_table_name = db.shorten_name(u'products_product_images')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False)),
            ('image', models.ForeignKey(orm[u'products.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'image_id'])


    models = {
        u'products.image': {
            'Meta': {'object_name': 'Image'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"})
        },
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'description': ('tinymce.models.HTMLField', [], {}),
            'dimensions': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['products']