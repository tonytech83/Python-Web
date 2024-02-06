from django.shortcuts import render, redirect

from forms_basic.web.forms import DemoForm, EmployeeForm
from forms_basic.web.models import Employee


def index(request):
    if request.method == 'GET':
        form = DemoForm()
    else:
        form = DemoForm(request.POST)
        if form.is_valid():
            # data is valid, populate `cleaned_data`
            print(form.cleaned_data['first_name'])

            # use data

            # redirect to some URL
            return redirect('index')
        else:
            # data is invalid, populate `errors`
            pass

    context = {
        'employee_form': DemoForm(),
        'form': EmployeeForm(),
    }

    return render(request, 'web/index.html', context)


def index_modelform(request):
    form = EmployeeForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # directly save the data into DataBase
            form.save()

            redirect('index')

    context = {
        'form': form,
        'employees_list': Employee.objects.all(),
    }

    return render(request, 'web/index_modelform.html', context)


def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'GET':
        form = EmployeeForm(instance=employee)
    else:
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()

            return redirect('model-form')

    context = {
        'form': form,
        'employee': employee,
    }

    return render(request, 'web/employee_details.html', context)
