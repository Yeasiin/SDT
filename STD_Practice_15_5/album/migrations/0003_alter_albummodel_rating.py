# Generated by Django 5.1.2 on 2024-10-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_alter_albummodel_options_albummodel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
