# -*- coding: utf-8 -*-
__author__ = '许仕强'
# @Time    : 2018/8/13 11:00
# @Email   : austin@canway.net
from django.db.models.signals import post_migrate
from books.models import Author
from books import models as invite_app


# 定义receiver函数
def init_db(sender, **kwargs):
    if sender.name == 'Author.__name__':
        if not Author.objects.exists():
            Author.objects.create(author='小明', phone_num='1234567', email='qwe@qq.com')  # 当发送信号的模型是你要初始化的模型的时候，
            # 在进行数据库操作，不加判断的话，每一个模型都会调用


post_migrate.connect(init_db, sender=invite_app)
