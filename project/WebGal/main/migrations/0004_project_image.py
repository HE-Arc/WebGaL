# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='http://portfoliotheme.org/enigmatic/wp-content/uploads/sites/9/2012/07/placeholder1.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]