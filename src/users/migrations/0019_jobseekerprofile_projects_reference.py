# Generated by Django 3.1.2 on 2021-02-06 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20210205_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeekerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(blank=True, null=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_type', models.CharField(blank=True, choices=[('Personal', 'Personal'), ('Professional', 'Professional')], max_length=20, null=True)),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.jobseekerprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.jobseekerprofile')),
            ],
        ),
    ]