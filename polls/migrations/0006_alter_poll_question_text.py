# Generated by Django 4.0.1 on 2022-02-15 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='question_text',
            field=models.CharField(default='', max_length=255),
        ),
    ]
