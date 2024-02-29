from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


# Just add new fields
# class AppUser(AbstractUser):
#     age = models.IntegerField()

# Completely replace the User
# AbstractBaseUser - Register, Login
# PermissionsMixin - Permissions and Groups
# class AppUser(AbstractBaseUser, PermissionsMixin):
#     USERNAME_FIELD = 'email'  # Change the way of authentication -> email and password
