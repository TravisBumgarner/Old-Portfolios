# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0030_auto_20160924_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Author',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('photo', models.ImageField(upload_to='single_page_website/media/img/')),
                ('photography_portfolio_url', models.CharField(blank=True, max_length=100)),
                ('instagram_url', models.CharField(blank=True, max_length=100)),
                ('startup_url', models.CharField(blank=True, max_length=100)),
                ('linkedin_url', models.CharField(blank=True, max_length=100)),
                ('resume_url', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
