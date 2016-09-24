# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0008_auto_20160918_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_Directory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('directory', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ('directory',),
            },
        ),
        migrations.RemoveField(
            model_name='post_project',
            name='images',
        ),
        migrations.RemoveField(
            model_name='post_project',
            name='published_date',
        ),
        migrations.AddField(
            model_name='post_project',
            name='headline_image',
            field=models.ImageField(upload_to='images_directory/CharField', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post_project',
            name='sub_images_directory',
            field=models.CharField(choices=[('BRO', 'Bronx'), ('BRK', 'Brooklyn'), ('QNS', 'Queens'), ('MAN', 'Manhattan')], default='', max_length=1),
            preserve_default=False,
        ),
    ]
