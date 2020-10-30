from django.shortcuts import render


from .models import Job


def all_jobs(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
    }
    return render(request, 'jobs/all.html', context)