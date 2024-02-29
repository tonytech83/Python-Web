from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

# Just add new fields
# class AppUser(AbstractUser):
#     age = models.IntegerField()

# Completely replace the User
# class AppUser(AbstractBaseUser):
#     pass
