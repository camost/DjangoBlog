# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-26 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20160726_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='archivo',
            field=models.FileField(upload_to='img/imagenes'),
        ),
    ]