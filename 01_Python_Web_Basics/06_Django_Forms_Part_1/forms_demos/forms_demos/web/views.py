from django.shortcuts import render

from forms_demos.web.forms import PersonForm
from forms_demos.web.models import Person


def index(request):
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

    return render(request, 'index.html', context)
