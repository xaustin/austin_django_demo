# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods_sn', models.CharField(default=b'', max_length=50, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x94\xaf\xe4\xb8\x80\xe8\xb4\xa7\xe5\x8f\xb7')),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x90\x8d')),
                ('click_num', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\x95\xb0')),
                ('sold_num', models.IntegerField(default=0, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe9\x94\x80\xe5\x94\xae\xe9\x87\x8f')),
                ('fav_num', models.IntegerField(default=0, verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f\xe6\x95\xb0')),
                ('goods_num', models.IntegerField(default=0, verbose_name=b'\xe5\xba\x93\xe5\xad\x98\xe6\x95\xb0')),
                ('market_price', models.FloatField(default=0, verbose_name=b'\xe5\xb8\x82\xe5\x9c\xba\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('shop_price', models.FloatField(default=0, verbose_name=b'\xe6\x9c\xac\xe5\xba\x97\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('goods_brief', models.TextField(max_length=500, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xae\x80\xe7\x9f\xad\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('ship_free', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x89\xbf\xe6\x8b\x85\xe8\xbf\x90\xe8\xb4\xb9')),
                ('is_new', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x96\xb0\xe5\x93\x81')),
                ('is_hot', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\x83\xad\xe9\x94\x80')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u5546\u54c1',
                'verbose_name_plural': '\u5546\u54c1',
            },
        ),
    ]
