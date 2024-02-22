from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia.profiles.validators import validate_starts_with_letter


class Profile(models.Model):
    MIN_FIRST_NAME_LENGTH = 2
    MAX_FIRST_NAME_LENGTH = 25

    MIN_LAST_NAME_LENGTH = 1
    MAX_LAST_NAME_LENGTH = 35

    MAX_EMAIL_LENGTH = 40

    MIN_PASSWORD_LENGTH = 8
    MAX_PASSWORD_LENGTH = 20

    DEFAULT_AGE = 18

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_FIRST_NAME_LENGTH),
            validate_starts_with_letter,
        ),
        null=False,
        blank=False,
        verbose_name="First Name"
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_LAST_NAME_LENGTH),
            validate_starts_with_letter,
        ),
        null=False,
        blank=False,
        verbose_name="Last Name"
    )

    email = models.EmailField(
        max_length=MAX_EMAIL_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        validators=(
            MinLengthValidator(MIN_PASSWORD_LENGTH),
        ),
        null=False,
        blank=False,
        help_text=f'*Password length requirements: {MIN_PASSWORD_LENGTH} to {MAX_PASSWORD_LENGTH} characters'
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL',
    )

    age = models.PositiveIntegerField(
        default=DEFAULT_AGE,
        null=True,
        blank=True,
    )
