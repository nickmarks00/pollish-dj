# Generated by Django 4.0.1 on 2022-07-18 23:54

from django.db import migrations, models
import pollish.models


class Migration(migrations.Migration):

    dependencies = [
        ('pollish', '0029_alter_poll_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=pollish.models.Community.community_directory_path),
        ),
    ]
