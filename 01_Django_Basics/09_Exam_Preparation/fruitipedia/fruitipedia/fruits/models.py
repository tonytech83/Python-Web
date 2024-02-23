from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia.fruits.validators import validate_only_letters
from fruitipedia.profiles.models import Profile


class Fruit(models.Model):
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
            validate_only_letters,
        ),
        unique=True,
        null=False,
        blank=False,
        error_messages={
            'unique': 'This field must be unique. Custom error message.',
        },
        verbose_name='Name',
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    description = models.TextField(
        null=False,
        blank=False,
        verbose_name='Description',
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
        verbose_name="Nutrition",
    )

    owner = models.ForeignKey(
        to=Profile,
        # TODO: To fix `on_delete` if needed
        on_delete=models.CASCADE,
    )
