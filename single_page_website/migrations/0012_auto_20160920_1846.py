# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0011_auto_20160918_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_image',
            name='project',
            field=models.ForeignKey(default='', to='single_page_website.Post_Project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project_image',
            name='image',
            field=models.ImageField(upload_to='images_directory/'),
        ),
    ]
