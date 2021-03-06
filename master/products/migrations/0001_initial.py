# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemType'
        db.create_table(u'products_itemtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('nama_keren', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('waktu_input', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'products', ['ItemType'])

        # Adding model 'Items'
        db.create_table(u'products_items', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('waktu_input', self.gf('django.db.models.fields.DateTimeField')()),
            ('waktu_modif', self.gf('django.db.models.fields.DateTimeField')()),
            ('tipe_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.ItemType'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('harga_beli', self.gf('django.db.models.fields.IntegerField')()),
            ('harga_jual', self.gf('django.db.models.fields.IntegerField')()),
            ('harga_minimal', self.gf('django.db.models.fields.IntegerField')()),
            ('stok', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('img', self.gf('django.db.models.fields.CharField')(default='/static/img/empty.png', max_length=64)),
        ))
        db.send_create_signal(u'products', ['Items'])

        # Adding model 'Pelanggan'
        db.create_table(u'products_pelanggan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('alamat', self.gf('django.db.models.fields.TextField')(default='')),
            ('no_hape', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'products', ['Pelanggan'])

        # Adding model 'Penjualan'
        db.create_table(u'products_penjualan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('waktu_beli', self.gf('django.db.models.fields.DateTimeField')()),
            ('harga', self.gf('django.db.models.fields.IntegerField')()),
            ('jumlah', self.gf('django.db.models.fields.IntegerField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('harga_total', self.gf('django.db.models.fields.IntegerField')()),
            ('pelanggan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Pelanggan'])),
            ('kode', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'products', ['Penjualan'])

        # Adding model 'Log'
        db.create_table(u'products_log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('waktu_input', self.gf('django.db.models.fields.DateTimeField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('data', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'products', ['Log'])


    def backwards(self, orm):
        # Deleting model 'ItemType'
        db.delete_table(u'products_itemtype')

        # Deleting model 'Items'
        db.delete_table(u'products_items')

        # Deleting model 'Pelanggan'
        db.delete_table(u'products_pelanggan')

        # Deleting model 'Penjualan'
        db.delete_table(u'products_penjualan')

        # Deleting model 'Log'
        db.delete_table(u'products_log')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'products.items': {
            'Meta': {'object_name': 'Items'},
            'harga_beli': ('django.db.models.fields.IntegerField', [], {}),
            'harga_jual': ('django.db.models.fields.IntegerField', [], {}),
            'harga_minimal': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.CharField', [], {'default': "'/static/img/empty.png'", 'max_length': '64'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'stok': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tipe_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.ItemType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'waktu_input': ('django.db.models.fields.DateTimeField', [], {}),
            'waktu_modif': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'products.itemtype': {
            'Meta': {'object_name': 'ItemType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'nama_keren': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'waktu_input': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        u'products.log': {
            'Meta': {'object_name': 'Log'},
            'data': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'waktu_input': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'products.pelanggan': {
            'Meta': {'object_name': 'Pelanggan'},
            'alamat': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'no_hape': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'products.penjualan': {
            'Meta': {'object_name': 'Penjualan'},
            'harga': ('django.db.models.fields.IntegerField', [], {}),
            'harga_total': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jumlah': ('django.db.models.fields.IntegerField', [], {}),
            'kode': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'pelanggan': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Pelanggan']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'waktu_beli': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['products']