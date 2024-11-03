# Generated by Django 5.1.2 on 2024-11-03 04:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_categorymodel_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorymodel',
            name='tasks',
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Category Name'),
        ),
    ]
