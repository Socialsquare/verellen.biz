# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MenuContent.login_label'
        db.add_column(u'content_menucontent', 'login_label',
                      self.gf('django.db.models.fields.CharField')(default='Log in', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MenuContent.login_label'
        db.delete_column(u'content_menucontent', 'login_label')


    models = {
        u'content.aboutcontent': {
            'Meta': {'object_name': 'AboutContent'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'content.footercontent': {
            'Meta': {'object_name': 'FooterContent'},
            'contact_body': ('tinymce.models.HTMLField', [], {}),
            'contact_header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
        }
    }

    complete_apps = ['content']