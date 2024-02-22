from django.core.validators import MinLengthValidator
from django.db import models

from my_plant_app.profiles.validators import validate_first_letter_capitalized


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 10
    MAX_NAME_LENGTH = 20

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH),
        ),
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        verbose_name="First Name",
        max_length=MAX_NAME_LENGTH,
        validators=(
            validate_first_letter_capitalized,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=MAX_NAME_LENGTH,
        validators=(
            validate_first_letter_capitalized,
        ),
        null=False,
        blank=False,
    )

    profile_pic = models.URLField(
        verbose_name="Profile Picture",
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
