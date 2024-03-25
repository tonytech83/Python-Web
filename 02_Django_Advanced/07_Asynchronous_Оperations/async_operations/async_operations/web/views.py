from django.contrib.auth import get_user_model
from django.shortcuts import render

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

    return render(request, 'web/index.html', context)
