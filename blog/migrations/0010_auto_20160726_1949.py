# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-26 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_post_titulillo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='archivo',
            field=models.FileField(upload_to='imagenes'),
        ),
    ]
