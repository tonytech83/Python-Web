from django.shortcuts import render
from django.http import HttpResponse


def show_department_by_id(request, department_id):
    department_name = ''

    if department_id == 1:
        department_name = 'Developers'
    elif department_id == 2:
        department_name = 'Trainers'

    html = "<html><body><h1>" \
           "Department Name: %s, Department ID: %s" \
           "</h1></body></html>" \
           % (department_name, department_id)

    return HttpResponse(html)
