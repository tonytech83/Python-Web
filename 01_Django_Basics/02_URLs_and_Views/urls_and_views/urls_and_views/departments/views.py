import time

from django.http import HttpResponse
from django.shortcuts import render


def index(request, *args, **kwargs):
    return HttpResponse(f"Hello, world. The time is {time.time()}")


def department_1_details(request):
    return HttpResponse(f"Department 1")


def department_2_details(request):
    return HttpResponse(f"Department 2")


def department_details(request, pk):
    return HttpResponse(f"Department by ID: {pk}")


def department_details_by_name(request, name):
    return HttpResponse(f"Department with name: {name}")
