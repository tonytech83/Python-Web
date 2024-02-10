from django.core.validators import MinLengthValidator
from django.db import models


class Category(models.Model):
    MIN_NAME_LENGTH = 3
    MAX_NAME_LENGTH = 50

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_NAME_LENGTH),
        ),
    )

    def __str__(self):
        return self.name


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

    category = models.ForeignKey(
        to=Category,
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
    )
