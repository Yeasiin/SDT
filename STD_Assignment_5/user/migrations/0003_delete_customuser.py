# Generated by Django 5.1.2 on 2025-01-20 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_delete_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
