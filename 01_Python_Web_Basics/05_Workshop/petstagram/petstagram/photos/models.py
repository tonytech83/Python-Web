# photos/models.py

from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size


class Photo(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='media/photos/',
        validators=[
            validate_file_size,
        ],
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=[
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ],
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True
    )

    date_of_publication = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    # One-to-One relations
    # ...

    # One-to-Many relations
    #  ...

    # Many-to-Many relations
    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
    )
