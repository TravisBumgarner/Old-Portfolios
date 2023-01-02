# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('single_page_website', '0021_auto_20160924_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('headline_image', models.ImageField(upload_to='images_directory/headline_images')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Project_Category',
        ),
        migrations.RenameModel(
            old_name='Tool',
            new_name='Project_Tool',
        ),
        migrations.RemoveField(
            model_name='post_project',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post_project',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='post_project',
            name='tools',
        ),
        migrations.RemoveField(
            model_name='project_image',
            name='project',
        ),
        migrations.DeleteModel(
            name='Post_Project',
        ),
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(to='single_page_website.Project_Category'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_images',
            field=models.ForeignKey(to='single_page_website.Project_Image'),
        ),
        migrations.AddField(
            model_name='project',
            name='tools',
            field=models.ManyToManyField(to='single_page_website.Project_Tool'),
        ),
    ]
