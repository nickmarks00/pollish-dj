# Generated by Django 4.0.1 on 2022-02-15 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollish', '0006_alter_poll_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='question_text',
            field=models.TextField(default=''),
        ),
    ]
