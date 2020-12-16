from django.shortcuts import render

from users.forms import myForm

from .forms import ContactForm

from jobs.models import Industry

from django.contrib import messages


def index(request):
    if request.POST:
        if 'contact' in request.POST:
            contact_form = ContactForm(request.POST or None)
            form = myForm()
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, 'Contact Form Submitted.')
        else:
            form = myForm(request.POST or None)
            if form.is_valid():
                form.save(request)
                form = myForm()
            contact_form = ContactForm()
    else:
        contact_form = ContactForm()
        form = myForm()


    industries = Industry.objects.all()
    print(request.POST)
    context = {
        'form': form,
        'industries': industries,
        'contact_form': contact_form,
    }
    # if form.is_valid():
    #     form.save(request)
    #     form = myForm()
    return render(request, 'index.html', context)