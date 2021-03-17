from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required 

from jobs.models import Job, JobApplication


def mainHiring(request):
    return render(request, 'hiring/main.html', {})


@login_required
def jobApplications(request):
    user = request.user
    jobs = Job.objects.filter(created_by=user)
    jobApps = JobApplication.objects.filter(job__in=jobs)
    # print(jobApplications)
    # print(type(jobApplications))
    if request.method == 'POST':
        print(request.POST)
        if 'reject' in request.POST:
            id = int(request.POST.get('id'))
            currentApplication = JobApplication.objects.get(id=id)
            currentApplication.selected = False
            currentApplication.save()
            return redirect('hiring:job_applications')
        elif 'unreject' in request.POST:
            id = int(request.POST.get('id'))
            currentApplication = JobApplication.objects.get(id=id)
            currentApplication.selected = None
            currentApplication.save()
            return redirect('hiring:job_applications')
        elif 'progress' in request.POST:
            id = int(request.POST.get('id'))
            currentApplication = JobApplication.objects.get(id=id)
            if currentApplication.shortlisted == None:
                currentApplication.shortlisted = True
                currentApplication.save()

            elif currentApplication.interviewed == None:
                currentApplication.interviewed = True
                currentApplication.save()

            elif currentApplication.selected == None:
                currentApplication.selected = True
                currentApplication.save()
            return redirect('hiring:job_applications')

    context = {
        'jobApplications': jobApps,
    }
    return render(request, 'hiring/job_applications.html', context)