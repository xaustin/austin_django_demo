# -*- coding: utf-8 -*-
from django.db import models


# 作者
class Author(models.Model):
    author = models.CharField(max_length=128, verbose_name=u'作者')
    phone_num = models.CharField(max_length=128, verbose_name=u'手机号码')
    email = models.CharField(max_length=128, verbose_name=u'邮箱')
    school = models.CharField(max_length=50, verbose_name=u'学校', blank=True, null=True)
    # emails = models.CharField(max_length=128, verbose_name=u'邮箱', blank=True)

    def to_dic(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])


# 书籍
class Books(models.Model):
    book_name = models.CharField(max_length=128, verbose_name=u'书籍名称')
    book_introduce = models.CharField(max_length=256, verbose_name=u'书籍介绍')
    book_user = models.ManyToManyField(Author, through='AuthBook', verbose_name=u'书籍作者')
    book_finish_time = models.DateTimeField(verbose_name=u'书籍完成时间')


# 出版社
class Press(models.Model):
    press_name = models.CharField(max_length=128, verbose_name=u'出版社名称')
    press_address = models.CharField(max_length=128, verbose_name=u'出版社地址')


# 使用多对多的中间模型
# 当我们使用多对多的中间模型之后，add(),remove(),create()这些方法都会被禁用，
# 所以在创建这种类型的关系的时候唯一的方法就是通过创建中间模型的实例
class AuthBook(models.Model):
    book_info = models.ForeignKey(Books, on_delete=models.CASCADE)  # 级联删除
    user_info = models.ForeignKey(Author, on_delete=models.CASCADE)  # 级联删除


class Colors(models.Model):
    colors = models.CharField(max_length=10)  # 颜色

    def __str__(self):
        return self.colors


class Ball(models.Model):
    color = models.OneToOneField("Colors")  # 与颜色表为一对一，颜色表为母表
    description = models.CharField(max_length=10)  # 颜色描述

    def __str__(self):
        return self.description


class Clothes(models.Model):
    color = models.ForeignKey("Colors")  # 与颜色表为外键，颜色表为母表
    # color = models.ForeignKey("Colors", null=True,on_delete=models.SET_NULL))  # 可为空，如果外键被删后，
    # 子表数据此字段置空而不是直接删除这条数据，同理也可以SET_DEFAULT,需要此字段有默认值
    description = models.CharField(max_length=10)  # 描述

    def __str__(self):
        return self.description


class Child(models.Model):
    name = models.CharField(max_length=10)  # 姓名
    favor = models.ManyToManyField('Colors')  # 与颜色表为多对多