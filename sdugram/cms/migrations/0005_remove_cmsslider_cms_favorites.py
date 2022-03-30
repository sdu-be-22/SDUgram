

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_alter_cmsslider_cms_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cmsslider',
            name='cms_favorites',
        ),
    ]
