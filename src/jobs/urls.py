from django.urls import path

from .views import jobs_view, jobs_by, job_detail, create_jobs, my_jobs, search, my_job_applications

app_name = 'jobs'

urlpatterns = [
    path('all', jobs_view, name='all'),
    path('industry/<id>', jobs_by, name='industry'),
    path('job/<id>', job_detail, name='detail'),
    path('create', create_jobs, name='create'),
    path('my-jobs', my_jobs, name='my'),
    path('search', search, name='search'),
    path('my-job-applications', my_job_applications, name='my-apps'),
]