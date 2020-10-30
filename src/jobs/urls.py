from django.urls import path

from .views import all_jobs

app_name = 'jobs'

urlpatterns = [
    path('all', all_jobs, name='all')
]