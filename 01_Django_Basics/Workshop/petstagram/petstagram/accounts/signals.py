from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from petstagram.accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    # created = False, when update
    # created = True, when create
    if not created:
        return

    # Variant 1: Eager save
    Profile.objects.create(user=instance)

    # Variant 2
    # profile = Profile(user=instance)
    # other code
    # profile.save()
