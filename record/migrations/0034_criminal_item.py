# Generated by Django 4.1.2 on 2022-10-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0033_alter_criminal_timeleft'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminal',
            name='Item',
            field=models.CharField(blank=True, choices=[('Money', 'Money'), ('Food', 'Food'), ('Cloth', 'Cloth')], max_length=20, null=True),
        ),
    ]
