# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0003_auto_20160918_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project_image',
            options={'ordering': ('title',)},
        ),
    ]
