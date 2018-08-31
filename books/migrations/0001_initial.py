# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=128, verbose_name='\u4f5c\u8005')),
                ('phone_num', models.CharField(max_length=128, verbose_name='\u624b\u673a\u53f7\u7801')),
                ('email', models.CharField(max_length=128, verbose_name='\u90ae\u7bb1')),
            ],
        ),
        migrations.CreateModel(
            name='Ball',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_name', models.CharField(max_length=128, verbose_name='\u4e66\u7c4d\u540d\u79f0')),
                ('book_introduce', models.CharField(max_length=256, verbose_name='\u4e66\u7c4d\u4ecb\u7ecd')),
                ('book_finish_time', models.DateTimeField(verbose_name='\u4e66\u7c4d\u5b8c\u6210\u65f6\u95f4')),
                ('book_user', models.ManyToManyField(to='books.Author', verbose_name='\u4e66\u7c4d\u4f5c\u8005', through='books.AuthBook')),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('colors', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('press_name', models.CharField(max_length=128, verbose_name='\u51fa\u7248\u793e\u540d\u79f0')),
                ('press_address', models.CharField(max_length=128, verbose_name='\u51fa\u7248\u793e\u5730\u5740')),
            ],
        ),
        migrations.AddField(
            model_name='clothes',
            name='color',
            field=models.ForeignKey(to='books.Colors'),
        ),
        migrations.AddField(
            model_name='child',
            name='favor',
            field=models.ManyToManyField(to='books.Colors'),
        ),
        migrations.AddField(
            model_name='ball',
            name='color',
            field=models.OneToOneField(to='books.Colors'),
        ),
        migrations.AddField(
            model_name='authbook',
            name='book_info',
            field=models.ForeignKey(to='books.Books'),
        ),
        migrations.AddField(
            model_name='authbook',
            name='user_info',
            field=models.ForeignKey(to='books.Author'),
        ),
    ]
