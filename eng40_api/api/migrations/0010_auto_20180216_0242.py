# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-16 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20180216_0235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='photo',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='image',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='api.Project'),
        ),
        migrations.AlterField(
            model_name='link',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='link', to='api.Project'),
        ),
    ]