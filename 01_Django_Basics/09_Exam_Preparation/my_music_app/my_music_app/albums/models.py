from django.core.validators import MinValueValidator
from django.db import models

from my_music_app.profiles.models import Profile


class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MAX_GENRE_LENGTH = 30
    MIN_PRICE = 0.0

    class MusicGenre(models.TextChoices):
        POP = 'Pop Music', 'Pop Music'
        JAZZ = 'Jazz Music', 'Jazz Music'
        RNB = 'R&B Music', 'R&B Music'
        ROCK = 'Rock Music', 'Rock Music'
        COUNTRY = 'Country Music', 'Country Music'
        DANCE = 'Dance Music', 'Dance Music'
        HIP_HOP = 'Hip Hop Music', 'Hip Hop Music'
        OTHER = 'Other', 'Other'

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
        unique=True,
    )

    artist_name = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        null=False,
        blank=False,
        choices=MusicGenre.choices,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
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

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )
