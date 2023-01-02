# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0041_auto_20161007_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='video',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project_image',
            name='project',
            field=models.ForeignKey(related_name='project_image', to='single_page_website.Project'),
        ),
    ]
