# Generated by Django 4.1.2 on 2022-11-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prison', '0011_alter_prison_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourtName', models.CharField(blank=True, choices=[('court one', 'court one'), ('court 2', 'court 2')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reason', models.CharField(blank=True, choices=[('በአመክሮ', 'በአመክሮ'), ('በነፃ ተሰናበተ', 'በነፃ ተሰናበተ'), (' በበቂ ተሰናበተ', ' በበቂ ተሰናበተ'), ('ክሱ የተቋረጠ', 'ክሱ የተቋረጠ'), ('በዋስ ተለቀቀ', 'በዋስ ተለቀቀ'), ('በገደብ ተፈታ', 'በገደብ ተፈታ'), ('የገንዘብ ቅጣት', 'የገንዘብ ቅጣት'), ('ፍርዱን ጨርሶ ተፈታ', 'ፍርዱን ጨርሶ ተፈታ'), ('ዋስትና የተፈቀደለት', 'ዋስትና የተፈቀደለት'), ('ሞቶ ፋይሉ ተዘጋ', 'ሞቶ ፋይሉ ተዘጋ'), ('የጠፋ', 'የጠፋ'), ('በይቅርታ', 'በይቅርታ')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place', models.CharField(blank=True, choices=[('sebatamit', 'sebatamit'), ('kalitie', 'kalitie'), ('d/markos', 'd/markos'), ('shewarobit', 'sewarobit'), ('ziway', 'ziway')], max_length=200, null=True)),
            ],
        ),
    ]