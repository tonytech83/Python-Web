from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from custom_auth.accounts.models import AccountUserProfile

UserModel = get_user_model()


# 2
# class AccountUserCreationForm(auth_forms.UserCreationForm):
#     class Meta(auth_forms.UserCreationForm.Meta):
#         model = UserModel
#         # fields = auth_forms.UserCreationForm.Meta.fields + ('age',)


# 3.1
class AccountUserCreationForm(auth_forms.UserCreationForm):
    age = forms.IntegerField()

    # Other fields from `Profile`

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = AccountUserProfile(
            user=user,
            age=self.cleaned_data['age'],
        )

        if commit:
            profile.save()

        return user
