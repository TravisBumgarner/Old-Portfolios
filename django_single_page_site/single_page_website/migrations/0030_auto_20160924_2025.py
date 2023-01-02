# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0029_project_title_computer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='headline_image',
            field=models.ImageField(upload_to='single_page_website/media/img/'),
        ),
        migrations.AlterField(
            model_name='project_image',
            name='image',
            field=models.ImageField(upload_to='single_page_website/media/img/'),
        ),
    ]
