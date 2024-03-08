from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from custom_auth.accounts.models import Profile

UserModel = get_user_model()

"""
Signals should be imported in `apps.py` for current Django app
In `settings.py` we should registered our Django apps with `.apps.<APP>Config`
    - 'custom_auth.accounts.apps.AccountsConfig',
    - 'custom_auth.web.apps.WebConfig',
"""


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    create_profile(instance, created)
    send_successful_registration_email(instance)


def create_profile(instance, created):
    if not created:
        return

    # profile = instance.profile

    if Profile.objects.filter(pk=instance.pk).first():
        return

    Profile.objects.create(user=instance)


def send_successful_registration_email(user):
    pass
