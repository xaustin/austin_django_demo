# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='school',
            field=models.CharField(max_length=50, null=True, verbose_name='\u5b66\u6821', blank=True),
        ),
    ]
