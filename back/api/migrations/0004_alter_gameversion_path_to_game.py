# Generated by Django 4.2.2 on 2023-06-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_game_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameversion',
            name='path_to_game',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
