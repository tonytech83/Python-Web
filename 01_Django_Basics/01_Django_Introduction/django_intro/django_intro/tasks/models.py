from django.db import models


class Task(models.Model):
    MAX_TITLE_LENGTH = 120

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
    )

    description = models.TextField()

    done = models.BooleanField(default=False)