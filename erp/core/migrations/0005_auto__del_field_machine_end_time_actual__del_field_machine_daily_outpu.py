# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Machine.end_time_actual'
        db.delete_column(u'core_machine', 'end_time_actual')

        # Deleting field 'Machine.daily_output_actual'
        db.delete_column(u'core_machine', 'daily_output_actual')


    def backwards(self, orm):
        # Adding field 'Machine.end_time_actual'
        db.add_column(u'core_machine', 'end_time_actual',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Machine.daily_output_actual'
        db.add_column(u'core_machine', 'daily_output_actual',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    models = {
        u'core.configuration': {
            'Meta': {'object_name': 'Configuration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notify_time_interval': ('django.db.models.fields.IntegerField', [], {}),
            'page_size': ('django.db.models.fields.IntegerField', [], {'default': '10'})
        },
        u'core.machine': {
            'Meta': {'object_name': 'Machine'},
            'daily_output_estimated': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'efficiency': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'end_time_estimated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'length_available': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Material']"}),
            'no': ('django.db.models.fields.IntegerField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Product']"}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'speed': ('django.db.models.fields.IntegerField', [], {}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'take_up_rate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tou_wen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.TouWen']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Type']"}),
            'wei_mi': ('django.db.models.fields.FloatField', [], {})
        },
        u'core.material': {
            'Meta': {'object_name': 'Material'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.touwen': {
            'Meta': {'object_name': 'TouWen'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.type': {
            'Meta': {'object_name': 'Type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['core']