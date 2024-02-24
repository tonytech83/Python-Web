from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed.cars.validators import validate_car_year
from world_of_speed.profiles.models import Profile


class CarTypes(models.TextChoices):
    RALLY = 'Rally', 'Rally'
    OPEN_WHEEL = 'Open-wheel', 'Open-wheel'
    KART = 'Kart', 'Kart'
    DRAG = 'Drag', 'Drag'
    OTHER = 'Other', 'Other'


class Car(models.Model):
    MAX_TYPE_LENGTH = 10

    MIN_MODEL_LENGTH = 1
    MAX_MODEL_LENGTH = 15

    MIN_PRICE = 1.0

    car_type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        choices=CarTypes.choices,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        validators=(
            MinLengthValidator(MIN_MODEL_LENGTH),
        ),
        null=False,
        blank=False,
    )
    year = models.IntegerField(
        validators=(
            validate_car_year,
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        unique=True,
        null=False,
        blank=False,
        error_messages={
            'unique': 'This image URL is already in use! Provide a new one.'
        },
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE),
        ),
        null=False,
        blank=False,
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )
