# Generated by Django 2.1 on 2018-08-14 20:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 14, 13, 28, 36, 13025)),
        ),
    ]
