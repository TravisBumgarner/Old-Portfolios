# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0009_auto_20160918_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_project',
            name='sub_images_directory',
            field=models.CharField(choices=[('mech-project', 'Mechanical Engineering'), ('web-project', 'Web Design & Development'), ('electrical-project', 'Electrical Engineering'), ('electrical-project', 'Computer Programming'), ('civil-project', 'Civil Engineering'), ('other-project', 'Other Projects')], max_length=30),
        ),
    ]
