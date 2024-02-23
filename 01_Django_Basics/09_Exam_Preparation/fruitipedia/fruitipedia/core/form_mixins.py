class RemoveLabelMixin:
    no_label_fields = ()

    def _apply_no_label_fields(self):
        for field_name in self.no_label_fields:
            self.fields[field_name].label = ''


class SetPlaceholderMixin:
    placeholders = {}

    def _set_placeholders(self):
        for field_name in self.placeholders:
            self.fields[field_name].widget.attrs['placeholder'] = self.placeholders[field_name]


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
