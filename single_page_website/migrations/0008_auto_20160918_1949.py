# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0007_auto_20160918_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_project',
            old_name='image',
            new_name='images',
        ),
    ]
