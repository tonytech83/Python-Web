from django.http import HttpResponse
from django.shortcuts import render

from forms_demos.web.forms import TodoForm, TodoCreateFrom


# With Django Form
def index(request):
    if request.method == 'GET':
        form = TodoForm()
    else:
        form = TodoForm(request.POST)

        if form.is_valid():
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)


# With Django ModelForm
def index2(request):
    if request.method == 'GET':
        form = TodoCreateFrom()
    else:
        form = TodoCreateFrom(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }

    return render(request, 'index2.html', context)
