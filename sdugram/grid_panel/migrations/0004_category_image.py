# Generated by Django 4.0.2 on 2022-04-03 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grid_panel', '0003_category_advt_advt_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img/category'),
        ),
    ]