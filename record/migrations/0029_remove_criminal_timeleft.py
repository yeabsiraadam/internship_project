# Generated by Django 4.1 on 2022-10-11 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0028_criminal_timeleft'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criminal',
            name='TimeLeft',
        ),
    ]