from django.contrib.auth import get_user_model
from django.db import models

"""
Variants:
1. Use the default user as-is
2. Extend the default user and add more stuff (Extend the `AbstractUser` class)
3. Rewrite the whole user (Extend the `AbstractBaseUser` class)
"""

UserModel = get_user_model()


# 1. Proxy Model - Hardly used, only adds custom behaviour
class AccountsUserProxy(UserModel):
    class Meta:
        proxy = True
        ordering = ('first_name',)

    def some_custom_behavior(self):
        pass
