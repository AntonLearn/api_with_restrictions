# Generated by Django 5.0.7 on 2024-08-06 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_advertisement_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='draft',
            field=models.BooleanField(default=True),
        ),
    ]
