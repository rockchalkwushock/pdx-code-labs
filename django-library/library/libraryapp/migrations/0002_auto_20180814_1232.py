# Generated by Django 2.0 on 2018-08-14 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 14, 12, 32, 27, 658006)),
        ),
    ]
