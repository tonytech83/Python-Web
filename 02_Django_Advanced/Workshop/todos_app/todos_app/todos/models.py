from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class TodoState(models.TextChoices):
    DONE = "Done", "Done"
    NOT_DONE = "Not Done", "Not Done"


class Category(models.Model):
    MAX_NAME_LENGTH = 15
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Todo(models.Model):
    MAX_TITLE_LENGTH = 30
    MAX_STATE_LENGTH = max(len(x) for _, x in TodoState.choices)

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    state = models.CharField(
        max_length=MAX_STATE_LENGTH,
        choices=TodoState.choices,
        default=TodoState.NOT_DONE,
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
