# Generated by Django 4.0.1 on 2022-05-14 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_user_following'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id']},
        ),
    ]
