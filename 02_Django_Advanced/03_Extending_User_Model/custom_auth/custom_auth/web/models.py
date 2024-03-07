from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


# No table needed
class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ModelOne(AuditModel, models.Model):
    field = models.CharField(
        max_length=20,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.DO_NOTHING,
    )
