# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-26 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160726_1934'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadFile',
        ),
        migrations.AddField(
            model_name='post',
            name='archivo',
            field=models.FileField(default='a', upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='titulillo',
            field=models.CharField(default='q', max_length=50),
            preserve_default=False,
        ),
    ]
