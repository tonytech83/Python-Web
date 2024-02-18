from django import forms

from petstagram.core.form_mixins import ReadOnlyFieldsFormMixin, DisabledFieldsFormMixin
from petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', 'description', 'location', 'tagged_pets')


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(ReadOnlyFieldsFormMixin, DisabledFieldsFormMixin, PhotoBaseForm):
    readonly_fields = ('photo',)
    disabled_fields = ('photo',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._apply_readonly_fields()
        self._apply_disabled_fields()
