# Generated by Django 4.0.2 on 2022-03-26 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grid_panel', '0002_advt_advt_dt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='advt',
            name='advt_cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='grid_panel.category'),
        ),
    ]
