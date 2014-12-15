# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CarouselImage'
        db.create_table(u'content_carouselimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_file', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'content', ['CarouselImage'])

        # Removing M2M table for field products on 'HomeContent'
        db.delete_table(db.shorten_name(u'content_homecontent_products'))

        # Adding M2M table for field carousel_images on 'HomeContent'
        m2m_table_name = db.shorten_name(u'content_homecontent_carousel_images')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('homecontent', models.ForeignKey(orm[u'content.homecontent'], null=False)),
            ('carouselimage', models.ForeignKey(orm[u'content.carouselimage'], null=False))
        ))
        db.create_unique(m2m_table_name, ['homecontent_id', 'carouselimage_id'])


    def backwards(self, orm):
        # Deleting model 'CarouselImage'
        db.delete_table(u'content_carouselimage')

        # Adding M2M table for field products on 'HomeContent'
        m2m_table_name = db.shorten_name(u'content_homecontent_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('homecontent', models.ForeignKey(orm[u'content.homecontent'], null=False)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['homecontent_id', 'product_id'])

        # Removing M2M table for field carousel_images on 'HomeContent'
        db.delete_table(db.shorten_name(u'content_homecontent_carousel_images'))


    models = {
        u'content.aboutcontent': {
            'Meta': {'object_name': 'AboutContent'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'content.carouselimage': {
            'Meta': {'object_name': 'CarouselImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'content.footercontent': {
            'Meta': {'object_name': 'FooterContent'},
            'contact_body_left': ('tinymce.models.HTMLField', [], {}),
            'contact_body_right': ('tinymce.models.HTMLField', [], {}),
            'contact_header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'newsletter_header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'social_body': ('tinymce.models.HTMLField', [], {}),
            'social_header': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'content.homecontent': {
            'Meta': {'object_name': 'HomeContent'},
            'carousel_images': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['content.CarouselImage']", 'symmetrical': 'False'}),
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
        }
    }

    complete_apps = ['content']