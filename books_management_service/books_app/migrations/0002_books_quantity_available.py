# Generated by Django 5.0.3 on 2024-03-29 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='quantity_available',
            field=models.IntegerField(default=0),
        ),
    ]
