from django import forms

from petstagram.core.form_mixins import DisabledFormMixin
from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    # placeholders or other widgets can be modified from `__init__`
    # with less code
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Pet name'

    class Meta:
        model = Pet

        # if we want to change the order of fields, we should use `fields`
        fields = ('name', 'date_of_birth', 'personal_photo',)

        # not the case, we want to skip 'slug', because it is auto generated
        # fields = '__all__'

        # exclude = ('slug',)

        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {
            # 'name': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Pet name',
            #     }
            # ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date'
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            ),
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(DisabledFormMixin, PetBaseForm):
    disabled_fields = ('name', 'date_of_birth', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
