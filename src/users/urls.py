from django.urls import path

from .views import employer_profile, jobseeker_profile, profile_create


urlpatterns = [
    path('employer/profile', employer_profile, name='employer_profile'),
    path('jobseeker/profile', jobseeker_profile, name='jobseeker_profile'),
    path('create-profile/', profile_create, name='create_profile'),
]