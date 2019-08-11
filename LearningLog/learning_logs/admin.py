# -*- encoding:utf-8 -*-
from django.contrib import admin
from .models import Topic, Entry


class TopicAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_added', 'text']


class EntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'date_added', 'topic_id']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)
