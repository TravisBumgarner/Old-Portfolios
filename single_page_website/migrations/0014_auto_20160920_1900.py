# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0013_auto_20160920_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('human_display_category', models.CharField(max_length=100)),
                ('html_class_display_category', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('human_display_category',),
            },
        ),
        migrations.AlterModelOptions(
            name='tool',
            options={'ordering': ('human_display_tool',)},
        ),
        migrations.RenameField(
            model_name='tool',
            old_name='tool',
            new_name='html_class_display_tool',
        ),
        migrations.RemoveField(
            model_name='post_project',
            name='sub_images_directory',
        ),
        migrations.AddField(
            model_name='tool',
            name='human_display_tool',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post_project',
            name='category',
            field=models.ManyToManyField(to='single_page_website.Category'),
        ),
    ]
