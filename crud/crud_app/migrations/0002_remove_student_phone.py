# Generated by Django 5.0.6 on 2024-07-08 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
    ]
