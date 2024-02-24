from django import forms

from world_of_speed.cars.models import Car
from world_of_speed.core.forms_mixins import SetPlaceholderMixin, ReadOnlyFieldsFormMixin


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreationForm(SetPlaceholderMixin, CarBaseForm):
    placeholders = {
        'image_url': 'https://...',
    }

    class Meta:
        model = Car
        fields = ('car_type', 'model', 'year', 'image_url', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_placeholders()


class CarEditForm(CarBaseForm):
    class Meta:
        model = Car
        exclude = ('owner',)


class CarDeleteForm(ReadOnlyFieldsFormMixin, CarBaseForm):
    readonly_fields = ('car_type', 'model', 'year', 'image_url', 'price')

    class Meta:
        model = Car
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.apply_readonly_fields()
