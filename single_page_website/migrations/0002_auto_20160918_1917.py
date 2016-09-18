# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='post_project',
            name='images',
            field=models.ForeignKey(to='single_page_website.Project_Image', default=''),
            preserve_default=False,
        ),
    ]
