# Generated by Django 3.1.2 on 2021-02-04 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_profile_current_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact_person',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_person_official_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_person_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]