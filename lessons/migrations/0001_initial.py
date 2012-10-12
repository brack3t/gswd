# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lesson'
        db.create_table('lessons_lesson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('order', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('video', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True)),
        ))
        db.send_create_signal('lessons', ['Lesson'])

        # Adding model 'Translation'
        db.create_table('lessons_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lesson', self.gf('django.db.models.fields.related.ForeignKey')(related_name='transcripts', to=orm['lessons.Lesson'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('intro', self.gf('django.db.models.fields.TextField')()),
            ('intro_html', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('body_html', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('transcript', self.gf('django.db.models.fields.TextField')()),
            ('transcript_html', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('lessons', ['Translation'])


    def backwards(self, orm):
        # Deleting model 'Lesson'
        db.delete_table('lessons_lesson')

        # Deleting model 'Translation'
        db.delete_table('lessons_translation')


    models = {
        'lessons.lesson': {
            'Meta': {'ordering': "['order', 'title']", 'object_name': 'Lesson'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        },
        'lessons.translation': {
            'Meta': {'object_name': 'Translation'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'body_html': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {}),
            'intro_html': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'lesson': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transcripts'", 'to': "orm['lessons.Lesson']"}),
            'transcript': ('django.db.models.fields.TextField', [], {}),
            'transcript_html': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        }
    }

    complete_apps = ['lessons']