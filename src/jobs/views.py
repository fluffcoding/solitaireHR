from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Job, Industry, JobApplication, choices

from .forms import JobForm, JobApplicationForm

from .filters import JobFilter

from django.contrib.auth.decorators import login_required

from django.db.models import Q

def jobs_view(request):
    jobs = Job.objects.all()
    # myFilter = JobFilter(request.GET, queryset=jobs)
    # jobs = myFilter.qs
    context = {
        'jobs': jobs,
        # 'myFilter': myFilter,
    }
    return render(request, 'jobs/all.html', context)



def jobs_by_industry(request, id):
    industry = Industry.objects.get(id=id)
    jobs = Job.objects.filter(industry=industry)
    context = {
        'jobs': jobs,
        'industry': industry,
    }
    return render(request, 'jobs/all.html', context)


def job_detail(request, id):
    job = Job.objects.get(id=id)
    form = JobApplicationForm(request.POST or None)
    if request.user.profile.job_seeker:
        can_apply = True
    else:
        can_apply = False
    if form.is_valid():
        form.cleaned_data['job_seeker'] = request.user
        form.cleaned_data['job'] = job
        print(form.cleaned_data)
        job_application = JobApplication(**form.cleaned_data)
        # job_application.save()
        job_application.save()
        return redirect('jobs:my')
        
    context = {
        'job': job,
        'form': form,
        'can_apply': can_apply,
    }
    return render(request, 'jobs/detail.html', context)


@login_required
def create_jobs(request):
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.cleaned_data['created_by'] = request.user
        job = Job(**form.cleaned_data)
        job.save()
        return redirect('jobs:all')
    context = {
        'form': form,
    }
    return render(request, 'jobs/create.html', context)
    

@login_required
def my_jobs(request):
    job_applications = JobApplication.objects.filter(job_seeker=request.user)
    context = {
        'job_applications' : job_applications,
    }
    return render(request, 'jobs/my_jobs.html', context)


def search(request):
    qs = Job.objects.all()
    data = request.GET.get('query')
    location = request.GET.get('location')
    if data != '' and data is not None:
        qs = qs.filter(Q(job_designation__icontains=data) | Q(job_description__icontains=data)).distinct()
    if location!='' and location is not None:
        qs = qs.filter(city__icontains=location)
    context = {
        'jobs': qs,
        'cities': choices['city'],
    }
    return render(request, 'jobs/all.html', context)


def my_job_applications(request):
    jobs = Job.objects.filter(created_by=request.user)
    job_applications = []
    if jobs:
        for job in jobs:
            job_applications += JobApplication.objects.filter(job=job)
    context = {
        'job_applications': job_applications,
    }
    return render(request, 'employer/my_job_applications.html', context)