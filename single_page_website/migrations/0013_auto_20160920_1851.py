# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0012_auto_20160920_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_project',
            name='sub_images_directory',
            field=models.CharField(choices=[('mech-project', 'Mechanical Engineering'), ('electrical-project', 'Electrical Engineering'), ('programming-project', 'Computer Programming'), ('web-project', 'Web Design & Development'), ('civil-project', 'Civil Engineering'), ('misc-project', 'Misc Projects')], max_length=30),
        ),
    ]
