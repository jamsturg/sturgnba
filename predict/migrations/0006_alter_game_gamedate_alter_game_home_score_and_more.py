# Generated by Django 4.1.5 on 2023-02-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0005_game_pmscore_alter_game_gamedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gamedate',
            field=models.CharField(default='2023-02-06', max_length=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_score',
            field=models.CharField(blank=True, default='0', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='visitor_score',
            field=models.CharField(blank=True, default='0', max_length=3, null=True),
        ),
    ]
