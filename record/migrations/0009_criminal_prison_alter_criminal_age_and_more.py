# Generated by Django 4.0.5 on 2022-09-01 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prison', '0002_delete_crime'),
        ('record', '0008_remove_criminal_prisonname'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminal',
            name='prison',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prison.prison'),
        ),
        migrations.AlterField(
            model_name='criminal',
            name='Age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='criminal',
            name='Imprisonment',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
