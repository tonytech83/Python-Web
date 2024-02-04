import random
from datetime import date

from django.shortcuts import render


class Person:
    def __init__(self, first_name, last_name, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


def index(request):
    person = Person('Ivan', 'Ivanov')
    context = {
        'title': 'Employees list',
        'person': {
            'first_name': 'John',
            'last_name': 'Doe'
        },
        'person_obj': person,
        'person_dict': person.__dict__,
        'names_list': ['name1', 'name2', 'name3'],
        'today': date.today(),

        # for use in tags demo
        'ages_list': [random.randrange(1, 100) for _ in range(6)],

        'get_params': request.GET,
    }

    return render(request, 'employees/index.html', context)


def employee_details(request, pk):
    context = {
        'pk': pk
    }
    return render(request, 'employees/details.html', context)
