# Generated by Django 4.0.1 on 2022-06-13 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollish', '0026_community_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='votes_registered',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
