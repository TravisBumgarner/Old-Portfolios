# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0006_auto_20160918_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_project',
            name='image',
            field=models.ForeignKey(to='single_page_website.Project_Image'),
        ),
    ]
