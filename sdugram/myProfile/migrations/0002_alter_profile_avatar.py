from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myProfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='profile_images/default_avatar.png', upload_to='media/profile_images/'),
        ),
    ]
