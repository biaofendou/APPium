# -*- encoding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
Django框架为我们提供ORM框架，可以自动根据代码生成数据表
1.定义模型类(在model.py中修改)
2.进行数据迁移
    2.1生成迁移文件(python manage.py makemigrations)
    2.2执行迁移(python manage.py migrate)
'''


class Topic(models.Model):
    """用户学习的分类"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # 在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题，不然会报错
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的有关某个分类的具体知识'"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # 指定模型的复数形式
    class Mate:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."
