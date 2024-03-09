from django.contrib.auth import get_user_model
from django.db import models

from petstagram.photos.models import Photo

UserModel = get_user_model()


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

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.RESTRICT,
    )


class PhotoLike(models.Model):
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.DO_NOTHING,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.RESTRICT,
    )
