from django.db import models


class Todo(models.Model):
    MAX_TITLE_LENGTH = 30

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False,
    )

    description = models.TextField()

    is_done = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )
