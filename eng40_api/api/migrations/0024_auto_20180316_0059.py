# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-16 00:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='gallery',
            field=models.ManyToManyField(blank=True, null=True, related_name='gallery', to='api.Image'),
        ),
        migrations.AlterField(
            model_name='project',
            name='preview_img',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preview_img', to='api.Image'),
        ),
    ]
