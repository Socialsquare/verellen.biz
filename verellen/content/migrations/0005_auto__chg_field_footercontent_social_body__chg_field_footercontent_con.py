# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FooterContent.social_body'
        db.alter_column(u'content_footercontent', 'social_body', self.gf('tinymce.models.HTMLField')())

        # Changing field 'FooterContent.contact_body'
        db.alter_column(u'content_footercontent', 'contact_body', self.gf('tinymce.models.HTMLField')())

    def backwards(self, orm):

        # Changing field 'FooterContent.social_body'
        db.alter_column(u'content_footercontent', 'social_body', self.gf('django.db.models.fields.TextField')())

        # Changing field 'FooterContent.contact_body'
        db.alter_column(u'content_footercontent', 'contact_body', self.gf('django.db.models.fields.TextField')())

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
        }
    }

    complete_apps = ['content']