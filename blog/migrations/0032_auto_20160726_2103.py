# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-27 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20160726_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='archivo',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
    ]
