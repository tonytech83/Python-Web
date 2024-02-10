from django.shortcuts import render

from forms_advanced.web.forms import PersonForm, PersonForm2, UpdatePersonForm, PersonFormReadOnly, PersonFormSet, \
    ExampleForm
from forms_advanced.web.models import Person


def index(request):
    mff_form = PersonForm2()
    person_form = PersonForm()
    update_person_form = UpdatePersonForm()
    readonly_person_form = PersonFormReadOnly()

    context = {
        'mff_form': mff_form,
        'person_form': person_form,
        'update_person_form': update_person_form,
        'readonly_person_form': readonly_person_form,
        'persons_list': Person.objects.all(),
    }

    return render(request, 'web/index.html', context)


def create_person(request):
    # `request.FILES` should be added to have ability to work with files
    form = PersonForm(request.POST, request.FILES, user=request.user)  # to take a user into the PersonForm

    if form.is_valid():
        form.save()


def show_formset(request):
    form_set = PersonFormSet()

    context = {
        'form_set': form_set,
    }

    return render(request, 'web/formsets.html', context)


def styling_demos(request):
    form = PersonForm()

    context = {
        'form': form,
    }

    return render(request, 'web/styling.html', context)


def crispy_form(request):
    form = ExampleForm()

    context = {
        'form': form,
    }

    return render(request, 'web/crispy_form.html', context)
