# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import single_page_website.models


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0005_auto_20160918_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Image',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AlterField(
            model_name='post_project',
            name='image',
            field=models.ImageField(upload_to='', verbose_name=single_page_website.models.Project_Image),
        ),
    ]
