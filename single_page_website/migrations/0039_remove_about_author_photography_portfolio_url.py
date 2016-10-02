# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0038_about_author_link_url_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about_author',
            name='photography_portfolio_url',
        ),
    ]
