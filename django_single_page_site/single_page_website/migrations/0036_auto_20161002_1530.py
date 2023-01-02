# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0035_auto_20160929_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_image1',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image10',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image11',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image12',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image13',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image14',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image15',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image3',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image4',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image5',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image6',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image7',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image8',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image9',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description1',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description10',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description11',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description12',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description13',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description14',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description15',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description3',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description4',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description5',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description6',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description7',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description8',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_image_description9',
        ),
        migrations.AddField(
            model_name='project_image',
            name='project',
            field=models.ForeignKey(to='single_page_website.Project', default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.CharField(max_length=50, default='Travis Bumgarner'),
        ),
    ]
