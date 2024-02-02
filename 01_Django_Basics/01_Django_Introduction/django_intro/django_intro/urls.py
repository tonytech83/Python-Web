from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # prefix '' for all URLs in `django_intro.tasks.urls`, i.e. no prefix
    path('', include('django_intro.tasks.urls')),
]

# `urls.py` contains only "/FULL/PATH"
# https://HOST:PORT/FULL/PATH?query=params&other=other_params#fragment


"""
Do always when creating new Django App

1. (Optional) Move Django App folder to project directory.
2. Create `urls.py` into Django app folder
3. Register this Django app's `urls.py` in the project's `urls.py`
4. Register this Django App into `settings.py`'s `INSTALLED_APPS`
"""
