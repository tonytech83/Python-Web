from django import forms

from my_music_app.albums.models import Album
from my_music_app.core.form_mixins import ReadOnlyFieldsFormMixin, DisabledFieldsFormMixin, AlbumFormMixin


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)

        labels = {
            'name': 'Album Name',
            'artist_name': 'Artist',
            'image_url': 'Image URL'
        }


class AlbumCreateForm(AlbumFormMixin, AlbumBaseForm):
    pass


class AlbumEditForm(AlbumFormMixin, AlbumBaseForm):
    pass


class AlbumDeleteForm(ReadOnlyFieldsFormMixin, DisabledFieldsFormMixin, AlbumBaseForm):
    readonly_fields = ('name', 'artist_name', 'description', 'image_url', 'price', 'genre',)

    # disabled_fields = ('name', 'artist_name', 'description', 'image_url', 'price', 'genre',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._apply_readonly_fields()
        self._apply_disabled_fields()
