# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CarouselImage.product'
        db.add_column(u'content_carouselimage', 'product',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CarouselImage.product'
        db.delete_column(u'content_carouselimage', 'product_id')


    models = {
        u'content.aboutcontent': {
            'Meta': {'object_name': 'AboutContent'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'content.carouselimage': {
            'Meta': {'object_name': 'CarouselImage'},
            'home_content': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.HomeContent']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'content.footercontent': {
            'Meta': {'object_name': 'FooterContent'},
            'contact_body_left': ('tinymce.models.HTMLField', [], {}),
            'contact_body_middle': ('tinymce.models.HTMLField', [], {}),
            'contact_body_right': ('tinymce.models.HTMLField', [], {}),
            'contact_header_left': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'contact_header_middle': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'contact_header_right': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'newsletter_header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'social_body': ('tinymce.models.HTMLField', [], {}),
            'social_header': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'content.homecontent': {
            'Meta': {'object_name': 'HomeContent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'content.menucontent': {
            'Meta': {'object_name': 'MenuContent'},
            'about_label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'partner_label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'products_label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'retailers_label': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'content.productcontent': {
            'Meta': {'object_name': 'ProductContent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_body': ('tinymce.models.HTMLField', [], {'default': "''"})
        },
        u'products.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'default': "'default_image'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Category']"}),
            'description': ('tinymce.models.HTMLField', [], {'default': "''", 'blank': 'True'}),
            'dimensions': ('tinymce.models.HTMLField', [], {'default': "''", 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tearsheet': ('django.db.models.fields.files.FileField', [], {'default': "'no_image.png'", 'max_length': '100'}),
            'tearsheet_metric': ('django.db.models.fields.files.FileField', [], {'default': "''", 'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['content']