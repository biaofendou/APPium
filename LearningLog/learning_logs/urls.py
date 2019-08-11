# -*- coding:utf-8 -*-
"""定义learning_logs的URL模式"""
from django.conf.urls import url
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 显示所有分类
    url(r'^topics/$', views.topics, name='topics'),
    # 显示特定分类的详情页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 添加新分类的页面
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 添加新条目的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 编辑条目的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    # 删除条目
    url(r'^delete_entry/(?P<entry_id>\d+)/$', views.delete_entry, name='delete_entry')
]
