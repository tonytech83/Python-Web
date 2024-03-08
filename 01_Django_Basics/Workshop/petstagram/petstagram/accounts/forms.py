from django.contrib.auth import forms as auth_forms

from petstagram.accounts.models import PetstagramUser


class PetstagramUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = PetstagramUser
        fields = ('email',)

    def save(self, *args, **kwargs):
        self.user = super().save(*args, **kwargs)

        return self.user
