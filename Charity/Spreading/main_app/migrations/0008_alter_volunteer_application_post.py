# Generated by Django 4.1.13 on 2024-06-29 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_volunteer_application_alter_cause_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer_application',
            name='post',
            field=models.FileField(null=True, upload_to='upload/Volunteer_form'),
        ),
    ]
