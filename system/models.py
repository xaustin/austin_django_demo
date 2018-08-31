# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User


# 用户
class User(AbstractUser):
    phone_number = models.CharField(max_length=40, blank=False, null=True, verbose_name=u'手机号')
    qq_number = models.CharField(max_length=40, blank=False, null=True, verbose_name=u'QQ号')

    class Meta:
        managed = True
        db_table = 'auth_user'


# 添加组是否启用
class ProfileGroupBase(type):
    def __new__(cls, name, bases, attrs):
        module = attrs.pop('__module__')
        parents = [b for b in bases if isinstance(b, ProfileGroupBase)]
        if parents:
            fields = []
            for obj_name, obj in attrs.items():
                if isinstance(obj, models.Field):
                    fields.append(obj_name)
                Group.add_to_class(obj_name, obj)
        return super(ProfileGroupBase, cls).__new__(cls, name, bases, attrs)


class ProfileGroup(object):
    __metaclass__ = ProfileGroupBase


class Ext(ProfileGroup):
    is_enable = models.BooleanField(default=False, verbose_name=u'是否启用', )


# 给权限添加自定义字段
class ProfilePermissonBase(type):
    def __new__(cls, name, bases, attrs):
        module = attrs.pop('__module__')
        parents = [b for b in bases if isinstance(b, ProfilePermissonBase)]
        if parents:
            fields = []
            for obj_name, obj in attrs.items():
                if isinstance(obj, models.Field):
                    fields.append(obj_name)
                Permission.add_to_class(obj_name, obj)
        return super(ProfilePermissonBase, cls).__new__(cls, name, bases, attrs)


class ProfilePermisson(object):
    __metaclass__ = ProfilePermissonBase


class Extend(ProfilePermisson):
    cate = models.CharField(max_length=40, verbose_name=u'权限分组',
                            null=True, blank=True)    # 用于页面上的权限分类展示
    order = models.IntegerField(null=True, blank=True)   # 用于页面上权限分类之后的展示的先后顺序
    per_name = models.CharField(max_length=40, verbose_name=u'权限名称', null=True, blank=True)