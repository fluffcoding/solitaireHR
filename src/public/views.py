from django.shortcuts import render

from users.forms import myForm



def index(request):
    form = myForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        form.save(request)
        form = myForm()
    return render(request, 'index.html', context)

