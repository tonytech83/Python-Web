from django.shortcuts import render

from forms_demos.web.forms import PersonForm, PersonCreateForm
from forms_demos.web.models import Person, Pet


def index_form(request):
    name = None

    # short record
    # form = NameForm(request.POST or None)

    if request.method == 'GET':
        form = PersonForm()
    else:  # request.method == 'POST'
        form = PersonForm(request.POST)
        if form.is_valid():
            '''
            'is_valid()`:
            - validates the form, returns True or False
            - fills `cleaned_data` which is dict with data from our form
            '''
            name = form.cleaned_data['your_name']
            Person.objects.create(
                name=name,
            )

    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'index_form.html', context)


def index_model_form(request):
    instance = Person.objects.get(pk=1)

    if request.method == 'GET':
        form = PersonCreateForm(instance=instance)
    else:
        form = PersonCreateForm(request.POST, instance=instance)

        if form.is_valid():
            # form.save() # same as code below

            pets = form.cleaned_data.pop('pets')
            person = Person.objects.create(
                **form.cleaned_data,
            )

            person.pets.set(pets)
            person.save()

    context = {
        'form': form,
    }

    return render(request, 'index_model_form.html', context)


def related_models_demo(request):
    pet = Pet.objects.get(pk=1)
    person = Person.objects.get(pk=10)

    # Person has `pets` field
    person_pets = person.pets.all()

    # Pet has no `person` field and we are using person_set
    pet_persons = pet.person_set.all()

    context = {
        'person_pets': person_pets,
        'pet_persons': pet_persons,
    }

    return render(request, 'demo_relations.html', context)
