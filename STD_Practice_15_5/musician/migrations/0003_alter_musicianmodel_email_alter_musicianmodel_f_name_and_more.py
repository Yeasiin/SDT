# Generated by Django 5.1.2 on 2024-10-30 20:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0002_alter_musicianmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicianmodel',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='musicianmodel',
            name='f_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='musicianmodel',
            name='l_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Last Name'),
        ),
    ]
