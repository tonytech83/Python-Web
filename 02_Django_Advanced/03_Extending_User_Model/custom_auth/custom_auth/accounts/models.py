from django.contrib.auth import get_user_model, models as auth_models

from django.db import models

"""
Variants:
1. Use the default user as-is
2. Extend the default user and add more stuff (Extend the `AbstractUser` class)
3. Rewrite the whole user (Extend the `AbstractBaseUser` class)
"""

UserModel = get_user_model()

""" 
1. Proxy Model - Hardly used, only adds custom behaviour (configuration from Meta and custom methods)
"""

# class AccountsUserProxy(UserModel):
#     class Meta:
#         proxy = True
#         ordering = ('first_name',)
#
#     def some_custom_behavior(self):
#         pass


# print(UserModel.objects.all())  # ordered by PK
# print(AccountsUserProxy.objects.all())  # ordered by `first_name`

"""2. Extend the build-in user model through `AbstractUser`:
    - Add `age` filed
    - Add `gender` filed
    - ...
Pros:
    - Simpler
    - No need to rewrite the Django auth system
"""

# class AccountsUser(auth_models.AbstractUser):
#     age = models.PositiveIntegerField(
#         null=True,
#         blank=True,
#     )


"""
3. Extend the default user model through a One-to-One relationship with a `Profile` model:
    - Add `age` filed
    - Add `gender` filed
    - ...
    3.1. Use the build-in user model for auth
    3.2. Create our own user model
Pros:
    - Easier migration to an other auth model in the future
"""


# 3.1.
class AccountUserProfile(models.Model):
    """
    Keep all personal information about user
    """
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,  # profile_obj.pk == profile.user_id
    )

