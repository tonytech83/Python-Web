from django.db import models


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
