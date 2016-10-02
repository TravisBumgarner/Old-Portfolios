# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0037_auto_20161002_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_author_link',
            name='url_path',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]
