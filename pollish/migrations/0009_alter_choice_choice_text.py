# Generated by Django 4.0.1 on 2022-02-16 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollish', '0008_alter_choice_choice_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default='', max_length=255),
        ),
    ]
