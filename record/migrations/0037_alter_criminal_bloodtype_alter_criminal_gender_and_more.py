# Generated by Django 4.1.2 on 2022-10-20 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0036_criminal_visitorsallowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminal',
            name='Bloodtype',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='criminal',
            name='Gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='criminal',
            name='VisitorsAllowed',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True),
        ),
    ]
