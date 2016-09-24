# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0004_auto_20160918_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_project',
            name='images',
        ),
        migrations.AddField(
            model_name='post_project',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Project_Image',
        ),
    ]
