# Generated by Django 4.1 on 2022-10-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0027_remove_criminal_time_left'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminal',
            name='TimeLeft',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
