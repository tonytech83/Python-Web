from django.contrib.auth import get_user_model

from rest_framework import generics as api_generic_views
from rest_framework.authtoken import views as token_views

from rest_advanced.accounts.serializers import UserRegistrationSerializer

UserModel = get_user_model()


class RegisterView(api_generic_views.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserRegistrationSerializer


# In Django
# class LoginView(LoginView)


# In Django REST framework
class LoginApiView(token_views.ObtainAuthToken):
    pass

# Logout view - No need. Handled on the client-side (React, Android, ...)
