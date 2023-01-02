# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0020_auto_20160924_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='skill_category',
            options={'ordering': ('title',)},
        ),
    ]
