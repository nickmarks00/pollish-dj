# Generated by Django 4.0.1 on 2022-03-27 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollish', '0017_alter_choice_users_alter_pollimage_image_src'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pollimage',
            old_name='image_src',
            new_name='image',
        ),
    ]
