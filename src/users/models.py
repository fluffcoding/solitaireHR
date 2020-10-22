from django.db import models

from django.contrib.auth import get_user_model

from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_jobseeker = models.BooleanField(null=True, blank=True)
    is_employer = models.BooleanField(null=True, blank=True)
    full_name = models.CharField(max_length=150, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

