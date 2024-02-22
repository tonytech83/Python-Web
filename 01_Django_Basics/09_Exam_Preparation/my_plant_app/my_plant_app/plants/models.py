from django.core.validators import MinLengthValidator
from django.db import models

from my_plant_app.plants.validators import validate_only_letters


class PlantTypes(models.TextChoices):
    OUTDOOR = 'Outdoor Plants', 'Outdoor Plants'
    INDOOR = 'Indoor Plants', 'Indoor Plants'


class Plant(models.Model):
    MAX_TYPE_LENGTH = 14

    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 20

    plant_type = models.CharField(
        verbose_name="Type",
        max_length=MAX_TYPE_LENGTH,
        choices=PlantTypes.choices,
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        verbose_name="Image URL",
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )
