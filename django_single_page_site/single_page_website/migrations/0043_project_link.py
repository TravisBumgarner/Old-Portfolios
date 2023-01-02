# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0042_auto_20161014_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Link',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('url_title', models.CharField(max_length=50)),
                ('url_path', models.CharField(max_length=300)),
                ('project', models.ForeignKey(to='single_page_website.Project', related_name='project_link')),
            ],
            options={
                'ordering': ('url_title',),
            },
        ),
    ]
