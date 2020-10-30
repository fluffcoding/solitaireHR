from django.shortcuts import render



def mainHiring(request):
    return render(request, 'hiring/main.html', {})