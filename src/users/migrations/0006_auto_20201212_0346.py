# Generated by Django 3.1.2 on 2020-12-12 03:46

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20201211_1257'),
        ('users', '0005_auto_20201211_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='branch_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='company_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='company_type',
            field=models.IntegerField(blank=True, choices=[(0, 'Sole Proprietarship'), (1, 'Public'), (2, 'Private'), (3, 'NGO')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='industry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.industry'),
        ),
        migrations.AddField(
            model_name='profile',
            name='number_of_employees',
            field=models.IntegerField(blank=True, choices=[(0, '1-10'), (1, '11-50'), (2, '51-200'), (3, '201-500'), (4, '500+')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='operating_since',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]