# Generated by Django 4.0.1 on 2022-02-25 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pollish', '0012_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_image',
        ),
        migrations.CreateModel(
            name='PollImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_src', models.ImageField(upload_to='poll_directory_path')),
                ('choice', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='pollish.choice')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pollish.poll')),
            ],
        ),
    ]
