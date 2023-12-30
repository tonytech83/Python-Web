from django import forms
from django.core.exceptions import ValidationError

from petstagram.common.models import PhotoLike, PhotoComment
from petstagram.core.form_mixins import DisabledFormMixin
from petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('date_of_publication',)


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('date_of_publication', 'photo')


class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disabled_fields()

    def save(self, commit=True):
        if commit:
            # Removes all relations to the photo, when the photo has tagged pets
            self.instance.tagged_pets.clear()  # many-to-many

            # Removes all relations to the photo, when the photo has likes
            (PhotoLike.objects
             .filter(photo_id=self.instance.id)
             .delete())  # one-to-many

            # Removes all relations to the photo, when the photo has comments
            (PhotoComment.objects
             .filter(to_photo_id=self.instance.id)
             .delete())  # one-to-many

            # Finally removes the photo
            self.instance.delete()

        return self.instance
