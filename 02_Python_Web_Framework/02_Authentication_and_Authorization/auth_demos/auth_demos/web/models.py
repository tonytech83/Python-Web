from django.contrib.auth import get_user_model
from django.db import models

# `get_user_model()` - returns current user model
UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    # ....

    # we split `Profile` and `User`, because `first_name` or 'last_name` is not a part of auth process
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
    )
