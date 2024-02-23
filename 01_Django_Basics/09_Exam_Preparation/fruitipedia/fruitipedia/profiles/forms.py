from django import forms

from fruitipedia.core.form_mixins import RemoveLabelMixin, SetPlaceholderMixin
from fruitipedia.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreatForm(RemoveLabelMixin, SetPlaceholderMixin, ProfileBaseForm):
    no_label_fields = ('first_name', 'last_name', 'email', 'password')
    placeholders = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'email': 'Email',
        'password': 'Password'
    }

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._apply_no_label_fields()
        self._set_placeholders()


class ProfileEditForm(SetPlaceholderMixin, ProfileBaseForm):
    placeholders = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'image_url': 'Image ULR',
        'age': 'Age'
    }

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url', 'age')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._set_placeholders()
