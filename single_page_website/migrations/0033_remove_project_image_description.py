# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0032_auto_20160929_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_image',
            name='description',
        ),
    ]
