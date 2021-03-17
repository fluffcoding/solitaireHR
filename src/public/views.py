from django.shortcuts import render, redirect

from users.forms import myForm

from .forms import ContactForm, AnonContactForm

from jobs.models import Industry, choices

from django.contrib import messages

from .models import Contact


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
    context = {
        'form': form,
        'industries': industries,
        'contact_form': contact_form,
        'cities': choices['city']
    }
    # if form.is_valid():
    #     form.save(request)
    #     form = myForm()
    return render(request, 'index.html', context)



def contact_view(request):
    if request.user.is_authenticated:
        contacted = Contact.objects.filter(user=request.user)
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('contact')
        context = {
            'form': form,
            'contacted': contacted
        }
    else:
        form = AnonContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('contact')

        context = {
            'form': form,
        }
    return render(request, 'contact.html', context)