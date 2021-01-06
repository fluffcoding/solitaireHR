from django.shortcuts import redirect
from django.http import HttpResponse

def require_employer(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.profile.is_employer:
            return HttpResponse('This page is only accessible for employers. Go to your profile settings to change your user type.')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def require_jobseeker(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.profile.is_jobseeker:
            return HttpResponse('This page is only accessible for job seekers. Go to your profile settings to change your user type.')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


