# Generated by Django 4.1.2 on 2022-10-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0037_alter_criminal_bloodtype_alter_criminal_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminal',
            name='Personality',
            field=models.CharField(max_length=100, null=True),
        ),
    ]