from django.shortcuts import render, redirect

from forms_basic.web.forms import EmployeeForm


def index(request):
    if request.method == 'GET':
        form = EmployeeForm()
    else:
        form = EmployeeForm(request.POST)
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
        'employee_form': EmployeeForm(),
    }

    return render(request, 'web/index.html', context)
