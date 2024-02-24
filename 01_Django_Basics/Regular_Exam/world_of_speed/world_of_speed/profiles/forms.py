from django import forms

from world_of_speed.core.forms_mixins import HideHelpTextFormMixin
from world_of_speed.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreationForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileEditForm(HideHelpTextFormMixin, ProfileBaseForm):
    help_text_fields = ('age',)

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)

        self.hide_help_text_fields()


class ProfileDeleteForm(ProfileBaseForm):
    pass
