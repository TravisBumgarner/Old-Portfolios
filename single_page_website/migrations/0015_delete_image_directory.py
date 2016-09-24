# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0014_auto_20160920_1900'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image_Directory',
        ),
    ]
