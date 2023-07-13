# Generated by Django 4.1.2 on 2022-11-07 15:32

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0041_rename_release_criminal_reason_for_release'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminal',
            name='Category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Criteria1', 'Criteria1'), ('Criteria2', 'Criteria2')], max_length=20, null=True),
        ),
    ]
