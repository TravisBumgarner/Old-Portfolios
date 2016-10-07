# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0040_auto_20161005_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_author_link',
            name='link_image',
            field=models.ImageField(upload_to='single_page_website/media/img/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='headline_image',
            field=models.ImageField(upload_to='single_page_website/media/img/'),
        ),
    ]
