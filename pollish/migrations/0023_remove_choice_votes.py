# Generated by Django 4.0.1 on 2022-04-02 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollish', '0022_alter_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
    ]
