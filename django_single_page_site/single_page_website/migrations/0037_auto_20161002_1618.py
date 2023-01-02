# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0036_auto_20161002_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Author_Link',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('url_title', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('url_title',),
            },
        ),
        migrations.RemoveField(
            model_name='about_author',
            name='instagram_url',
        ),
        migrations.RemoveField(
            model_name='about_author',
            name='linkedin_url',
        ),
        migrations.RemoveField(
            model_name='about_author',
            name='resume_url',
        ),
        migrations.RemoveField(
            model_name='about_author',
            name='startup_url',
        ),
        migrations.AddField(
            model_name='about_author_link',
            name='about',
            field=models.ForeignKey(to='single_page_website.About_Author'),
        ),
    ]
