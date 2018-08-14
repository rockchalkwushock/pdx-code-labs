# Generated by Django 2.0 on 2018-08-14 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0002_auto_20180814_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='checked_out',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 14, 13, 44, 25, 99450)),
        ),
    ]
