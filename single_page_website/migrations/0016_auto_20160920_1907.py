# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0015_delete_image_directory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_project',
            old_name='category',
            new_name='categories',
        ),
    ]
