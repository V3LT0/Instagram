# Generated by Django 5.1.3 on 2024-12-15 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofiles',
            name='followers',
        ),
    ]
