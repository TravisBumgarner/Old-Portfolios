# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-16 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20180316_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='gallery',
            field=models.ManyToManyField(blank=True, related_name='gallery', to='api.Image'),
        ),
    ]
