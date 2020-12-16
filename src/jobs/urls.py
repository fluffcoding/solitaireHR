from django.urls import path

from .views import jobs_view, jobs_by_industry, job_detail, create_jobs, my_jobs

app_name = 'jobs'

urlpatterns = [
    path('all', jobs_view, name='all'),
    path('industry/<id>', jobs_by_industry, name='industry'),
    path('job/<id>', job_detail, name='detail'),
    path('create', create_jobs, name='create'),
    path('my-jobs', my_jobs, name='my')
]