# Generated by Django 3.1.2 on 2020-12-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='applied',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='interviewed',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='selected',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='shortlisted',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]