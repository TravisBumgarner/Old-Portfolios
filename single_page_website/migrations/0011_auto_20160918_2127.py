# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0010_auto_20160918_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_project',
            name='headline_image',
            field=models.ImageField(upload_to='images_directory/'),
        ),
        migrations.AlterField(
            model_name='post_project',
            name='sub_images_directory',
            field=models.TextField(max_length=30, choices=[('mech-project', 'Mechanical Engineering'), ('web-project', 'Web Design & Development'), ('electrical-project', 'Electrical Engineering'), ('electrical-project', 'Computer Programming'), ('civil-project', 'Civil Engineering'), ('other-project', 'Other Projects')]),
        ),
    ]
