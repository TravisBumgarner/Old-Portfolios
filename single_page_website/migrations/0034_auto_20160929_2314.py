# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0033_remove_project_image_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_images',
        ),
        migrations.AddField(
            model_name='project',
            name='project_image1',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image10',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image11',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image12',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image13',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image14',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image15',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image2',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image3',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image4',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image5',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image6',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image7',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image8',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_image9',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='headline_image',
            field=models.ImageField(upload_to='single_page_website/media/img/', blank=True),
        ),
    ]
