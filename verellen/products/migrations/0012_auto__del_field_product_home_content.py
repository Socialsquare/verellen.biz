# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Product.home_content'
        db.delete_column(u'products_product', 'home_content_id')

        # Adding M2M table for field home_content on 'Product'
        m2m_table_name = db.shorten_name(u'products_product_home_content')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False)),
            ('homecontent', models.ForeignKey(orm[u'content.homecontent'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'homecontent_id'])


    def backwards(self, orm):
        # Adding field 'Product.home_content'
        db.add_column(u'products_product', 'home_content',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.HomeContent'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field home_content on 'Product'
        db.delete_table(db.shorten_name(u'products_product_home_content'))


    models = {
        u'content.homecontent': {
            'Meta': {'object_name': 'HomeContent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'products.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'products.image': {
            'Meta': {'object_name': 'Image'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"})
        },
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Category']"}),
            'description': ('tinymce.models.HTMLField', [], {}),
            'dimensions': ('tinymce.models.HTMLField', [], {}),
            'home_content': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['content.HomeContent']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['products.Image']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['products']