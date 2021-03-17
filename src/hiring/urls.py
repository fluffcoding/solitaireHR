from .views import mainHiring, jobApplications

from django.urls import path

app_name = 'hiring'


urlpatterns = [
    path('jobapplications', jobApplications, name='job_applications'),
    # path('hiring/', mainHiring, name='hiring'),
]