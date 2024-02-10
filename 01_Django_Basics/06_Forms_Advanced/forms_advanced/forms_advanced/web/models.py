from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


class Person(models.Model):
    MAX_NAME_LENGTH = 32
    MIN_NAME_LENGTH = 2

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),  # Build-in class validator
        ),
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
        ),
    )

    age = models.PositiveSmallIntegerField()

    profile_image = models.ImageField(
        upload_to='web/profile_images',
        null=True,
        blank=True,
    )

    created_by = models.ForeignKey(
        to=User,
        on_delete=models.DO_NOTHING,
        null=True,
    )
