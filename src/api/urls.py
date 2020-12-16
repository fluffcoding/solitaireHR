from django.urls import path

from .views import apiOverview, jobList, jobDetail

app_name = 'api'

urlpatterns = [
    path('', apiOverview, name='overview'),
    path('jobs', jobList, name='jobs'),
    path('job/<pk>', jobDetail, name='job-detail'),
]