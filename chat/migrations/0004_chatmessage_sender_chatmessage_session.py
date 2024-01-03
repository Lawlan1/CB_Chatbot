# Generated by Django 5.0 on 2023-12-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_delete_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='sender',
            field=models.CharField(choices=[('user', 'User'), ('bot', 'Bot')], default='user', max_length=4),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='session',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]