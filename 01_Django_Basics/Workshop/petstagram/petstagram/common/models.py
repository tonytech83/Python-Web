from django.db import models

from petstagram.photos.models import Photo


class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    photo = models.ForeignKey(
        to=Photo,
        on_delete=models.DO_NOTHING,
    )


class PhotoLike(models.Model):
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.DO_NOTHING,
    )