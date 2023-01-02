# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('single_page_website', '0017_auto_20160920_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill_Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(default='', to='single_page_website.Skill_Category'),
            preserve_default=False,
        ),
    ]
