from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class AccountUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = auth_forms.UserCreationForm.Meta.fields + ('age',)
