# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FooterContent'
        db.create_table(u'content_footercontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_header', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('contact_body', self.gf('django.db.models.fields.TextField')()),
            ('social_header', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('social_body', self.gf('django.db.models.fields.TextField')()),
            ('newsletter_header', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'content', ['FooterContent'])


    def backwards(self, orm):
        # Deleting model 'FooterContent'
        db.delete_table(u'content_footercontent')


    models = {
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