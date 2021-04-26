from django.db import models

from django.contrib.auth import get_user_model

from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
from jobs.models import choices, Industry

# from datetime import datetime
from django.utils import timezone
User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_jobseeker = models.BooleanField(null=True, blank=True)
    is_employer = models.BooleanField(null=True, blank=True)
    full_name = models.CharField(max_length=150, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True, default=timezone.now)
    country = CountryField(null=True, blank=True, default="PK")
    city = models.CharField(max_length=50, choices=choices['city'], null=True, blank=True)
    address_line1 = models.CharField(max_length=300, null=True, blank=True)
    address_line2 = models.CharField(max_length=300, null=True, blank=True)
    gender = models.CharField(max_length=50, choices=choices['gender'], null=True, blank=True)
    marital_status = models.CharField(max_length=50, choices=choices['marital_status'], null=True, blank=True)
    career_level = models.CharField(max_length=50, choices=choices['career_level'], null=True, blank=True)
    degree_level = models.CharField(max_length=50, choices=choices['degree_level'],null=True, blank=True)
    linked_in = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    mobile_phone = models.CharField(max_length=15, null=True, blank=True)
    zip_code = models.CharField(null=True, blank=True, max_length=20)
    
    preferred_job_designation = models.CharField(max_length=100, null=True, blank=True)
    preferred_job_city = models.CharField(max_length=50, choices=choices['city'], null=True, blank=True)
    expected_salary = models.CharField(max_length=50, choices=choices['salary'], null=True, blank=True)
    current_designation = models.CharField(max_length=100, null=True, blank=True)
    current_company = models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=50, choices=choices['experience'], null=True, blank=True)
    current_salary = models.CharField(max_length=50, choices=choices['salary'], null=True, blank=True)

    company = models.CharField(max_length=200,null=True, blank=True)
    company_type = models.CharField(max_length=50, choices=choices['company_type'],null=True, blank=True)
    company_country = CountryField(null=True, blank=True)
    city = models.CharField(max_length=50, choices=choices['city'],null=True, blank=True)
    branch_name = models.CharField(max_length=30,null=True, blank=True)
    company_website = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)
    address = models.CharField(max_length=200,null=True, blank=True)
    number_of_employees = models.CharField(max_length=50, choices=choices['number_of_employees'],null=True, blank=True)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL,null=True, blank=True)
    operating_since = models.CharField(max_length=10, null=True, blank=True)

    contact_person = models.CharField(max_length=150, null=True, blank=True)
    contact_person_phone = models.CharField(max_length=15,null=True, blank=True)
    contact_person_official_email = models.EmailField(null=True, blank=True)


class JobSeekerProfile(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    summary = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.profile.user.full_name}'s job seeker profile"


class Projects(models.Model):
    job_seeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class Reference(models.Model):
    job_seeker = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    reference_type = models.CharField(max_length=20, null=True, blank=True, choices=choices['reference_type'])
    name = models.CharField(max_length=150, null=True, blank=True)
    text = models.TextField(blank=True,null=True)





@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

