# Generated by Django 5.1.2 on 2025-01-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0002_borrowmodel_balance_after_record_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowmodel',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
