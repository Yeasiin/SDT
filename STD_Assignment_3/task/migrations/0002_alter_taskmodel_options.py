# Generated by Django 5.1.2 on 2024-11-02 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskmodel',
            options={'verbose_name': 'task', 'verbose_name_plural': 'tasks'},
        ),
    ]