from django import forms
from django.core.exceptions import ValidationError

from petstagram.core.form_mixins import ReadOnlyFieldsFormMixin
from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'date_of_birth', 'pet_photo',)

        labels = {
            'name': 'Pet name',
            'pet_photo': 'Link to image'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'pet_photo': forms.TextInput(attrs={'placeholder': 'Link to image'}),
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(ReadOnlyFieldsFormMixin, PetBaseForm):
    readonly_fields = ('date_of_birth',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._apply_readonly_fields()

        # self.fields['date_of_birth'].widget.attrs['readonly'] = True
        # self.fields['date_of_birth'].widget.attrs['disabled'] = True

    # Addition validation if `date_of_birth` is changed via HTML in browser
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']

        if date_of_birth != self.instance.date_of_birth:
            raise ValidationError('Date of birth is readonly!')

        return date_of_birth

    # Same as above but without error and always returns the initial `date_of_birth`
    # def clean_date_of_birth(self):
    #     return self.instance.date_of_birth


class PetDeleteForm(ReadOnlyFieldsFormMixin, PetBaseForm):
    readonly_fields = ('name', 'date_of_birth', 'pet_photo',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._apply_readonly_fields()
