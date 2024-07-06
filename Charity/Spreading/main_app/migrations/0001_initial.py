# Generated by Django 4.1.13 on 2024-07-06 12:36

from django.db import migrations, models
import django.db.models.deletion
import main_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=40)),
                ('profile', models.ImageField(upload_to='upload/cause')),
                ('summary', models.CharField(max_length=300)),
                ('info', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('number', models.CharField(max_length=20)),
                ('subject', models.TextField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile', models.ImageField(upload_to='upload/Events')),
                ('About', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=250)),
                ('Date', models.DateField(auto_now=True, null=True)),
                ('is_new', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='happy_customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(null=True, upload_to='upload/happy_customers')),
                ('position', models.CharField(max_length=10)),
                ('information', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=30)),
                ('subject', models.CharField(max_length=20)),
                ('post', models.FileField(null=True, upload_to='upload/Volunteer_form')),
                ('comment', models.CharField(max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dob', models.DateField(null=True)),
                ('salary', models.DecimalField(decimal_places=1, max_digits=6)),
                ('disabled', models.BooleanField(default=False)),
                ('profile', models.ImageField(default='employees/employee.png', null=True, upload_to=main_app.models.unique_img_name)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='multiple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(unique=True, upload_to='upload/multiple')),
                ('causes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.cause')),
            ],
        ),
    ]
