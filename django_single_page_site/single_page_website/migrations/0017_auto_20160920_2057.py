# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0016_auto_20160920_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='post_project',
            name='headline_image',
            field=models.ImageField(upload_to='images_directory/headline_images'),
        ),
    ]
