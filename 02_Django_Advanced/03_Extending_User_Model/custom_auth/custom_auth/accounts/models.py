from django.contrib.auth import get_user_model, models as auth_models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django.db import models

from custom_auth.accounts.managers import AccountUserManager

"""
Variants:
1. Use the default user as-is
2. Extend the default user and add more stuff (Extend the `AbstractUser` class)
3. Rewrite the whole user (Extend the `AbstractBaseUser` class)
"""

# UserModel = get_user_model()

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
# class AccountUserProfile(models.Model):
#     """
#     Keep all personal information about user
#     """
#     age = models.PositiveIntegerField(
#         null=True,
#         blank=True,
#     )
#
#     user = models.OneToOneField(
#         to=UserModel,
#         on_delete=models.CASCADE,
#         primary_key=True,  # profile_obj.pk == profile.user_id
#     )

# 3.2
class AccountUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    """
    Authentication information
    """
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        help_text=_(
            "Required a valid email address."
        ),
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now,
    )
    # Should be added to have access to admin console
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    # Dynamically set which field will be used for other (username) part of the **credentials**
    USERNAME_FIELD = "email"

    objects = AccountUserManager()


class Profile(models.Model):
    """
    User profile information
    """
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        to=AccountUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="profile",
    )
