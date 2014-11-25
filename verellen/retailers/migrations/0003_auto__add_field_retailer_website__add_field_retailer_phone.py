# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Retailer.website'
        db.add_column(u'retailers_retailer', 'website',
                      self.gf('django.db.models.fields.CharField')(default='http://www.verellen.biz', max_length=200),
                      keep_default=False)

        # Adding field 'Retailer.phone'
        db.add_column(u'retailers_retailer', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='1-234-567', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Retailer.website'
        db.delete_column(u'retailers_retailer', 'website')

        # Deleting field 'Retailer.phone'
        db.delete_column(u'retailers_retailer', 'phone')


    models = {
        u'retailers.retailer': {
            'Meta': {'object_name': 'Retailer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['retailers']