# Generated by Django 5.1.2 on 2025-01-19 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmodel',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='image',
            field=models.ImageField(upload_to='books/'),
        ),
    ]
