# Generated by Django 5.0 on 2023-12-25 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_response'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Response',
        ),
    ]
