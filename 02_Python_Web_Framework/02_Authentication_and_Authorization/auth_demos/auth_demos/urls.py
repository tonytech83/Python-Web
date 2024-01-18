from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('auth_demos.web.urls')),
]

# NEVER named your auth application `auth`
# Name it `app_auth` or `my_auth` or `PROJECT_NAME_auth`

# auth is using for both:
# - authentication (Who you are)
# - authorization (What you can do)

"""
Auth flow:

Authentication - The User send credentials to a system:
    - username & password; phone number & sms code; authentication code

Authorization - After authentication, the system authorize the user

"""

"""
Web1 (web app)
Web2 (web app)

Communication between Web1 and Web2 also should request auth and it happens through software key.
For example using GUID:
    - SoftUni_key = '1231-4221-4561-543367-11145f'
"""
