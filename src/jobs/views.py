from django.shortcuts import render, redirect


from .models import Job, Industry, JobApplication

from .forms import JobForm, JobApplicationForm

from .filters import JobFilter

from django.contrib.auth.decorators import login_required


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
    if form.is_valid():
        form.cleaned_data['job_seeker'] = request.user
        form.cleaned_data['job'] = job
        job_application = JobApplication(**form.cleaned_data)
        # job_application.save()
        job_application.save()
        return redirect('index')
    context = {
        'job': job,
        'form': form,
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