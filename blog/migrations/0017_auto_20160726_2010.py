# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-26 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20160726_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='archivo',
            field=models.FileField(upload_to='/home/camilo/Borrar/Blog/blog/static/images'),
        ),
    ]
