import random

from django.contrib.auth import get_user_model, authenticate
from django.shortcuts import render, redirect

# Better to use `UserModel` to take `User` instead of `from django.contrib.auth.models import User`
UserModel = get_user_model()


def index(request):
    suffix = random.randint(1, 1000)

    # Wrong way to create regular user, in this case password will be stored into database as plain-text
    # we can not authenticate the user with this password
    # UserModel.objects.create(
    #     username=f'TEST_{suffix}',
    #     password='Test_123456'
    # )

    # Proper way to create regular user - `create_user` method has function `make_password` which
    # turn a plain-text password into a hash for database storage
    UserModel.objects.create_user(
        username=f'TEST_{suffix}',
        password='Test_123456'
    )

    print(f'user login: {request.user}')

    user = UserModel.objects.get(username='admin')

    context = {
        'user': user,
    }
    return render(request, 'index.html', context)


def login(request):
    # `authenticate()` takes provided credentials and trying ot authenticate the user
    user = authenticate(
        username=f'TEST_301',
        password='Test_123456'
    )

    print(f'Logged in user: {user}')

    context = {
        user: user
    }

    return redirect('index')
