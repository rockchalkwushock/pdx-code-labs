# Generated by Django 2.0 on 2018-08-09 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_text', models.CharField(max_length=250, unique=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2018, 8, 9, 20, 54, 33, 228343))),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
