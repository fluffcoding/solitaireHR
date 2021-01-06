from django.urls import path

from .views import employer_profile, jobseeker_profile, profile_create, profile_redirect


urlpatterns = [
    path('employer/profile/<id>/', employer_profile, name='employer_profile'),
    path('jobseeker/profile/<id>/', jobseeker_profile, name='jobseeker_profile'),
    path('create-profile/', profile_create, name='create_profile'),
    path('profile-redirect/', profile_redirect, name='profile_redirect'),
]