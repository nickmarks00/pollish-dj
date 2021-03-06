# Generated by Django 4.0.1 on 2022-03-20 06:15

from django.conf import settings
from django.db import migrations, models
import pollish.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pollish', '0016_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='choices', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pollimage',
            name='image_src',
            field=models.ImageField(upload_to=pollish.models.PollImage.poll_directory_path),
        ),
    ]
