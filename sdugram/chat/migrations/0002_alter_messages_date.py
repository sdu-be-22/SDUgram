# Generated by Django 4.0.4 on 2022-04-20 22:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 20, 22, 2, 13, 456234)),
        ),
    ]