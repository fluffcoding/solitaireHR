from django.shortcuts import render

# Create your views here.

def mainCV(request):
    return render(request, 'cvwriting/main.html', {})