from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone

from django.utils.translation import gettext_lazy as _

from petstagram.accounts.managers import PetstagramUserManager

"""
Auth in Django:

1. Use build-in user - works out-of-the-box model
2. Use build-in user only for auth and define `Profile` model for user data
3. Define a custom user model for auth and define `Profile` model for user data
"""


# auth_models.AbstractUser


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    # password from `AbstractBaseUser`
    # last_login from `AbstractBaseUser`

    email = models.EmailField(
        _('email address'),
        unique=True,
        help_text=_(
            "Required. Valid email address."
        ),
        error_messages={
            "unique": _("A user with that email already exists."),
        },
        null=False,
        blank=False,
    )

    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    USERNAME_FIELD = "email"

    objects = PetstagramUserManager()


class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True
    )

    user = models.OneToOneField(
        to=PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return self.first_name or self.last_name
