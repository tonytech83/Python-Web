from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam_prep.web.model_validators import username_validator


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH),
            username_validator,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_LENGTH = 30
    MAX_GENRE_LENGTH = 30
    MIN_PRICE = 0.0

    GENRE_CHOISES = (
        (1, 'Pop Music'),
        (2, 'Jazz Music'),
        (3, 'R&B Music'),
        (4, 'Rock Music'),
        (5, 'Country Music'),
        (6, 'Dance Music'),
        (7, 'Hip Hop Music'),
        (8, 'Other')
    )

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        max_length=MAX_ARTIST_LENGTH,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=GENRE_CHOISES,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.ImageField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_PRICE),
        ),
    )
