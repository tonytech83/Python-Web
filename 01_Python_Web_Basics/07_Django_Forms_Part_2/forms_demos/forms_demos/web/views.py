from django.http import HttpResponse
from django.shortcuts import render, redirect

from forms_demos.web.forms import TodoForm, TodoCreateFrom, PersonCreateForm
from forms_demos.web.models import Person


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


def list_persons(request):
    context = {
        'persons': Person.objects.all(),
    }

    return render(request, 'list-persons.html', context)


def create_person(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:
        # When we work with media files:
        # 1. we should add `request.FILES` when creating the form
        # 2. In template form we should add `enctype="multipart/form-data"`
        # in this case `create-person.html`
        form = PersonCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('list persons')

    context = {
        'form': form,
    }

    return render(request, 'create-person.html', context)
