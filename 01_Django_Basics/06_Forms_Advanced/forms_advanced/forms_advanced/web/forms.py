from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelform_factory, modelformset_factory
from django.urls import reverse

from forms_advanced.web.models import Person


class ClassBootstrapFormMixin:
    def _set_class(self):
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class SetReadonlyFieldsMixin:
    """
    This mixin can be used to made fields read-only
    The mixin should be inherited into Form
    Inside the `__init__` of form we should call the method 'self._set_readonly_fields()`
    """

    # list of fields we want to make read-only
    readonly_fields = ()

    def _set_readonly_fields(self):
        for field in self.readonly_fields:
            self.fields[field].widget.attrs['readonly'] = True
            self.fields[field].widget.attrs['placeholder'] = 'This field is readonly'

            # for _, field in self.fields.items():
        #     field.widget.attrs['readonly'] = True
        #     field.widget.attrs['placeholder'] = 'This field is readonly'


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ('created_by',)

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')

        super().__init__(*args, **kwargs)

    # This method is used overall form cleaning/validation that involves multiple fields
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['first_name'] == cleaned_data['last_name']:
            raise ValidationError('Incorrect names')

        return cleaned_data

    # Additional validation on `first_name` field, which can't be done in model
    # def clean_first_name(self):
    #     pass

    # def clean_last_name(self):
    #     pass

    # def clean_age(self):
    #     pass

    # Overwrite `save()` method to add additional logic
    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.user.is_authenticated:
            instance.created_by = self.user

        instance.save()

        return instance

    labels = {
        'first_name': 'First name:',
    }

    error_messages = {
        'first_name': {
            'required': 'Please enter your first'
        },
    }


class UpdatePersonForm(PersonForm):
    # Customization of form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['age'].widget.attrs['readonly'] = True
        self.fields['age'].widget.attrs['placeholder'] = 'This field is readonly'


class PersonFormReadOnly(ClassBootstrapFormMixin, SetReadonlyFieldsMixin, PersonForm):
    readonly_fields = ('first_name', 'last_name', 'age')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._set_readonly_fields()
        self._set_class()


# Form creation via `modelform_factory` - used them when we don't want to have modification on the form
PersonForm2 = modelform_factory(Person, fields='__all__', widgets={})

# Creation of multiple forms of same type
PersonFormSet = modelformset_factory(Person, exclude=('created_by',), extra=2)


# Crispy form example
class ExampleForm(PersonForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForm'
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('crispy-form')
        self.helper.add_input(Submit('submit', 'Create Person'))
