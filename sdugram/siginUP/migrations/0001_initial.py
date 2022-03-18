from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=40)),
                ('photo', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=65)),
                ('password', models.CharField(max_length=150)),
                ('information', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='siginUP.userinformation')),
            ],
        ),
    ]
