# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170413_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='project',
            name='files',
            field=models.FileField(upload_to=main.models.upload_to),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to=main.models.upload_to),
        ),
    ]
