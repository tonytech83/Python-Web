from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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

    def __str__(self):
        return self.field


# Example of signals
@receiver(post_save, sender=ModelOne)
def model_one_created(sender, instance, created, **kwargs):
    print(sender, instance, created, kwargs)
