# Generated by Django 3.1.2 on 2020-12-12 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201212_0346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='designation',
        ),
    ]
