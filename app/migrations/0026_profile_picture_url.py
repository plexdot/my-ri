# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20160728_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture_url',
            field=models.URLField(blank=True),
        ),
    ]
