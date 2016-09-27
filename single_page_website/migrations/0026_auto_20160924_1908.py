# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0025_auto_20160924_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='headline_image',
            field=models.ImageField(upload_to='/single_page_website/static/images_directory/'),
        ),
    ]
