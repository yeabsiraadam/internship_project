# Generated by Django 4.1 on 2022-10-11 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0022_remove_criminal_timeleft'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminal',
            name='timeleft',
            field=models.IntegerField(null=True),
        ),
    ]
