from django import forms

from my_plant_app.core.forms_mixins import ReadOnlyFieldsFormMixin, DisabledFieldsFormMixin
from my_plant_app.plants.models import Plant


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantCreationForm(PlantBaseForm):
    pass


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(ReadOnlyFieldsFormMixin, DisabledFieldsFormMixin, PlantBaseForm):
    readonly_fields = ('plant_type', 'name', 'description', 'image_url', 'price')
    disabled_fields = ('plant_type', 'name', 'description', 'image_url', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._apply_readonly_fields()
        # self._apply_disabled_fields()
