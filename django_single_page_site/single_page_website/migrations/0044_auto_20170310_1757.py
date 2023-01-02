# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0043_project_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill_category',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='skill_category',
            name='order',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
