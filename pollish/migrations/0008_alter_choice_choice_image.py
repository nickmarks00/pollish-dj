# Generated by Django 4.0.1 on 2022-02-16 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollish', '0007_alter_poll_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_image',
            field=models.ImageField(blank=True, null=True, upload_to='poll_directory_path'),
        ),
    ]
