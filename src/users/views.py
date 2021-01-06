from jobs.models import Job, Industry

from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Profile

from django.contrib.auth.decorators import login_required
from .forms import profileForm1, profileForm2, profileForm3, profileForm4, profileForm5



@login_required
def profile_create(request):
    if not request.user.profile.is_jobseeker and not request.user.profile.is_employer:
        if request.method == 'POST':
            # print(request.POST)
            # print(request.POST.get('type'))
            profile = get_object_or_404(Profile, user=request.user)
            profile.full_name = request.POST.get('full_name')
            profile.date_of_birth = request.POST.get('date_of_birth')
            profile.gender = request.POST.get('gender')
            profile.website = request.POST.get('website')
            profile.mobile_phone = request.POST.get('mobile_phone')
            profile.country = request.POST.get('country')
            profile.city = request.POST.get('city')
            profile.address_line1 = request.POST.get('address_line1')
            profile.address_line2 = request.POST.get('address_line2')
            profile.zip_code = request.POST.get('zip_code')
            if request.POST.get('type') == 'jobseeker':
                profile.is_jobseeker = True
                profile.is_employer = False
                profile.preferred_job_designation = request.POST.get('preferred_job_designation')
                profile.preferred_job_city = request.POST.get('preferred_job_city')
                profile.expected_salary = request.POST.get('expected_salary')
                if request.POST.get('experience') == '':
                    profile.save()
                else:
                    profile.current_designation = request.POST.get('current_designation')
                    profile.current_company = request.POST.get('current_company')
                    profile.experience = request.POST.get('experience')
                    profile.save()
                return redirect('jobs:all')

            elif request.POST.get('type') == 'employer':
                profile.is_employer = True
                profile.is_jobseeker = False
                profile.company = request.POST.get('company')
                profile.company_type = request.POST.get('company_type')
                profile.company_country = request.POST.get('company_country')
                profile.city = request.POST.get('city')
                profile.branch_name = request.POST.get('branch_name')
                profile.company_website = request.POST.get('company_website')
                profile.phone = request.POST.get('phone')
                profile.address = request.POST.get('address')
                profile.number_of_employees = request.POST.get('number_of_employees')
                profile.operating_since = request.POST.get('operating since')
                profile.save()
                if request.POST.get('industry') != '' or None:
                    profile.industry = get_object_or_404(Industry, id=int(request.POST.get('industry')))
                return redirect('profile_redirect')

        form1 = profileForm1()
        form2 = profileForm2()
        form3 = profileForm3()
        form4 = profileForm4()
        form5 = profileForm5()
        context = {
            'form1': form1,
            'form2': form2,
            'form3': form3,
            'form4': form4,
            'form5': form5,
        }
        return render(request, 'users/profile_create.html', context)
    elif request.user.profile.is_jobseeker:
        # print('Is Job Seeker')
        return redirect('jobseeker_profile', request.user.id)
    elif request.user.profile.is_employer:
        # print('Is Employer')
        return redirect('employer_profile', request.user.id)


def profile_redirect(request):
    if request.user.profile.is_jobseeker:
        return redirect('jobseeker_profile', request.user.id)
    elif request.user.profile.is_employer:
        return redirect('employer_profile', request.user.id)
    else:
        return redirect('create_profile')


def employer_profile(request, id):
    user = User.objects.get(id=id)
    if user.profile.is_employer:
        jobs = Job.objects.filter(created_by=user)
        context = {
            'user': user,
            'jobs': jobs,
        }
        return render(request, 'account/employer_profile.html', context)
    else:
        return redirect('jobseeker_profile', id=id)


def jobseeker_profile(request, id):
    user = User.objects.get(id=id)
    if user.profile.is_jobseeker:
        return render(request, 'account/jobseeker_profile.html', {})
    elif user.profile.is_employer:
        return redirect('employer_profile', id=id)
    