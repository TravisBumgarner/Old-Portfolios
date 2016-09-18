# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0002_auto_20160918_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_image',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
