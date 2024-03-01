from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth import models as auth_models
from django.db import models


# Just add new fields
# to work in `settings.py` should be added `AUTH_USER_MODEL = 'accounts.AppUser'`
# class AppUser(auth_models.AbstractUser):
#     age = models.IntegerField()

# Completely replace the User
# AbstractBaseUser - Register, Login
# PermissionsMixin - Permissions and Groups
# class AppUser(AbstractBaseUser, PermissionsMixin):
#     USERNAME_FIELD = 'email'  # Change the way of authentication -> email and password
