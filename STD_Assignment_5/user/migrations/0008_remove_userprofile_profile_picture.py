# Generated by Django 5.1.2 on 2025-01-20 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_userprofile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
    ]
