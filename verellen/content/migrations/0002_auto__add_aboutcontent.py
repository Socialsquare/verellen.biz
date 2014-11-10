# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AboutContent'
        db.create_table(u'content_aboutcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'content', ['AboutContent'])


    def backwards(self, orm):
        # Deleting model 'AboutContent'
        db.delete_table(u'content_aboutcontent')


    models = {
        u'content.aboutcontent': {
            'Meta': {'object_name': 'AboutContent'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'content.footercontent': {
            'Meta': {'object_name': 'FooterContent'},
            'contact_body': ('django.db.models.fields.TextField', [], {}),
            'contact_header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'newsletter_header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'social_body': ('django.db.models.fields.TextField', [], {}),
            'social_header': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['content']