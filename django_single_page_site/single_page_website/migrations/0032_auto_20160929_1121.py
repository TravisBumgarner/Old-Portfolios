# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0031_about_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_date',
            field=models.DateTimeField(),
        ),
    ]
