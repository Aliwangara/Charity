# Generated by Django 5.0.6 on 2024-06-14 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_event_delete_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='Link',
        ),
    ]
