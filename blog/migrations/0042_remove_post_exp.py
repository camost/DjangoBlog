# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-27 20:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_auto_20160727_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='exp',
        ),
    ]