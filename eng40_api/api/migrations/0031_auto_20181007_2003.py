# Generated by Django 2.1.2 on 2018-10-07 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20180318_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
