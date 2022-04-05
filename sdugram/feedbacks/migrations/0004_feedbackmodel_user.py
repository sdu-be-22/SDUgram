from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0003_remove_feedbackmodel_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackmodel',
            name='user',
            field=models.CharField(default='Guest', max_length=40),
        ),
    ]
