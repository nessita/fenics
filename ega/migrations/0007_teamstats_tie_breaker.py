# Generated by Django 2.0.2 on 2018-06-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ega', '0006_auto_20180414_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamstats',
            name='tie_breaker',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
