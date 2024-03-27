from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render

from async_operations.web.tasks import slow_operation, send_example_email

"""
# Sync code

Servant 1:
1. Get coffee - 1 hour
2. Get milk - 1.5 hours
3. Prepare coffee with milk - 0.5 hours

Coffee with milk done in 3 hours

# Async code

Servant 1:                  | Servant 2:
1. Get coffee - 1 hour      | 1. Get milk - 1.5 hours

Servant 1 or Servant 2:
2. Prepare coffee with milk - 0.5 hours

Coffee with milk done in 2 hours
"""

UserModel = get_user_model()


def index(request):
    users_count = UserModel.objects.count()
    title = 'It works!'

    context = {
        'title': title,
        'users_count': users_count,
    }

    # for _ in range(500):
    #     slow_operation.delay()

    send_example_email.delay(users_count, title)

    # return render(request, 'web/index.html', context)
    return HttpResponse(str(context))
