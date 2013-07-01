# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Configuration'
        db.create_table(u'core_configuration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('notify_time_interval', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'core', ['Configuration'])

        # Adding model 'Type'
        db.create_table(u'core_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'core', ['Type'])

        # Adding model 'Product'
        db.create_table(u'core_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'core', ['Product'])

        # Adding model 'Material'
        db.create_table(u'core_material', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'core', ['Material'])

        # Adding model 'TouWen'
        db.create_table(u'core_touwen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'core', ['TouWen'])

        # Adding model 'Machine'
        db.create_table(u'core_machine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('no', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Type'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Product'])),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Material'])),
            ('tou_wen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.TouWen'])),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('wei_mi', self.gf('django.db.models.fields.FloatField')()),
            ('speed', self.gf('django.db.models.fields.IntegerField')()),
            ('efficiency', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('take_up_rate', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('daily_output_estimated', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('daily_output_actual', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time_estimated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_time_actual', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=10000, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Machine'])


    def backwards(self, orm):
        # Deleting model 'Configuration'
        db.delete_table(u'core_configuration')

        # Deleting model 'Type'
        db.delete_table(u'core_type')

        # Deleting model 'Product'
        db.delete_table(u'core_product')

        # Deleting model 'Material'
        db.delete_table(u'core_material')

        # Deleting model 'TouWen'
        db.delete_table(u'core_touwen')

        # Deleting model 'Machine'
        db.delete_table(u'core_machine')


    models = {
        u'core.configuration': {
            'Meta': {'object_name': 'Configuration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notify_time_interval': ('django.db.models.fields.IntegerField', [], {})
        },
        u'core.machine': {
            'Meta': {'object_name': 'Machine'},
            'daily_output_actual': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'daily_output_estimated': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'efficiency': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'end_time_actual': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'end_time_estimated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Material']"}),
            'no': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
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