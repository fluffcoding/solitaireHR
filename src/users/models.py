from django.db import models

from django.contrib.auth import get_user_model

from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
from jobs.models import choices, Industry

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_jobseeker = models.BooleanField(null=True, blank=True)
    is_employer = models.BooleanField(null=True, blank=True)
    full_name = models.CharField(max_length=150, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    city = models.IntegerField(choices=choices['city'], null=True, blank=True)
    address_line1 = models.CharField(max_length=300, null=True, blank=True)
    address_line2 = models.CharField(max_length=300, null=True, blank=True)
    gender = models.IntegerField(choices=choices['gender'], null=True, blank=True)
    marital_status = models.IntegerField(choices=choices['marital_status'], null=True, blank=True)
    career_level = models.IntegerField(choices=choices['career_level'], null=True, blank=True)
    degree_level = models.IntegerField(choices=choices['degree_level'],null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    mobile_phone = models.CharField(max_length=15, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    preferred_job_designation = models.CharField(max_length=100, null=True, blank=True)
    preferred_job_city = models.IntegerField(choices=choices['city'], null=True, blank=True)
    expected_salary = models.IntegerField(choices=choices['salary'], null=True, blank=True)
    current_designation = models.CharField(max_length=100, null=True, blank=True)
    current_company = models.CharField(max_length=100, null=True, blank=True)
    experience = models.IntegerField(choices=choices['experience'], null=True, blank=True)

    company = models.CharField(max_length=200,null=True, blank=True)
    company_type = models.IntegerField(choices=choices['company_type'],null=True, blank=True)
    company_country = CountryField(null=True, blank=True)
    city = models.IntegerField(choices=choices['city'],null=True, blank=True)
    branch_name = models.CharField(max_length=30,null=True, blank=True)
    company_website = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)
    address = models.CharField(max_length=200,null=True, blank=True)
    number_of_employees = models.IntegerField(choices=choices['number_of_employees'],null=True, blank=True)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL,null=True, blank=True)
    operating_since = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

