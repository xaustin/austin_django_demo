# -*- coding: utf-8 -*-
from django.db import models


# 我们之前一直在使用的Book.objects.all()之类的语句，其Book.objects就是所谓的Manager，
# 这是Django定义的用来管理模型的类，其中定义了很多函数，例如.all()。
# 有时候objects的功能不够用，我们就得写自己的Manager
# 额外增加额外Manager的方法
class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    num_pages = models.IntegerField(blank=True, null=True)
    objects = BookManager()

    def __unicode__(self):
        return self.title
