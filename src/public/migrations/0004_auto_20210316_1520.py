# Generated by Django 3.1.2 on 2021-03-16 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_contact_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Message',
            new_name='message',
        ),
    ]