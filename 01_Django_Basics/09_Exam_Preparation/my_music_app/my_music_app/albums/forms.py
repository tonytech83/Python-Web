from django import forms

from my_music_app.albums.models import Album
from my_music_app.core.form_mixins import ReadOnlyFieldsFormMixin, DisabledFieldsFormMixin


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner',)


class AlbumCreateForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Album Name'})
        self.fields['artist_name'].widget.attrs.update({'placeholder': 'Artist'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Description'})
        self.fields['image_url'].widget.attrs.update({'placeholder': 'Image URL'})
        self.fields['price'].widget.attrs.update({'placeholder': 'Price'})


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(ReadOnlyFieldsFormMixin, DisabledFieldsFormMixin, AlbumBaseForm):
    readonly_fields = ('name', 'artist_name', 'description', 'image_url', 'price', 'genre',)
    # disabled_fields = ('name', 'artist_name', 'description', 'image_url', 'price', 'genre',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._apply_readonly_fields()
        self._apply_disabled_fields()
