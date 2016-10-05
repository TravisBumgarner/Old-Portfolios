# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0039_remove_about_author_photography_portfolio_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_author_link',
            name='link_image',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AlterField(
            model_name='about_author_link',
            name='about',
            field=models.ForeignKey(related_name='about_author_link', to='single_page_website.About_Author'),
        ),
    ]
