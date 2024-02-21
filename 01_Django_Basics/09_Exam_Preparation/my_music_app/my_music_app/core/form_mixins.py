class ReadOnlyFieldsFormMixin:
    readonly_fields = ()

    def _apply_readonly_fields(self):
        for field_name in self.readonly_fields:
            self.fields[field_name].widget.attrs['readonly'] = True


class DisabledFieldsFormMixin:
    disabled_fields = ()

    def _apply_disabled_fields(self):
        for field_name in self.disabled_fields:
            self.fields[field_name].widget.attrs['disabled'] = True


class AlbumFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Album Name'
        self.fields['artist_name'].widget.attrs['placeholder'] = 'Artist'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['image_url'].widget.attrs['placeholder'] = 'Image URL'
        self.fields['price'].widget.attrs['placeholder'] = 'Price'
