from django import forms

from fruitipedia.core.form_mixins import RemoveLabelMixin, SetPlaceholderMixin, ReadOnlyFieldsFormMixin, \
    DisabledFieldsFormMixin
from fruitipedia.fruits.models import Fruit


class FruitBaseFrom(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class FruitCreatFrom(RemoveLabelMixin, SetPlaceholderMixin, FruitBaseFrom):
    no_label_fields = ('name', 'image_url', 'description', 'nutrition')
    placeholders = {
        'name': 'Fruit Name',
        'image_url': 'Fruit Image URL',
        'description': 'Fruit Description',
        'nutrition': 'Nutrition Info',
    }

    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description', 'nutrition')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._apply_no_label_fields()
        self._set_placeholders()


class FruitEditFrom(FruitBaseFrom):
    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description', 'nutrition')


class FruitDeleteFrom(ReadOnlyFieldsFormMixin, DisabledFieldsFormMixin, FruitBaseFrom):
    readonly_fields = ('name', 'image_url', 'description')
    disabled_fields = ('name', 'image_url', 'description')

    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._apply_readonly_fields()
        # self._apply_disabled_fields()
