# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-26 22:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_archivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='titulillo',
        ),
    ]
