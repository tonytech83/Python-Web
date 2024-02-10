from django.core.validators import MinLengthValidator
from django.db import models


class Todo(models.Model):
    MIN_TITLE_LENGTH = 3
    MAX_TITLE_LENGTH = 24

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        validators=(
            MinLengthValidator(MIN_TITLE_LENGTH),
        ),
        null=False,
        blank=False,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    deadline = models.DateTimeField(
        null=True,
        blank=True,
    )
