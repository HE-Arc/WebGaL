# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 21:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20170416_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='project',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
