# Generated by Django 4.1.2 on 2022-11-06 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0040_criminal_release_criminal_transfer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='criminal',
            old_name='Release',
            new_name='Reason_For_Release',
        ),
    ]
