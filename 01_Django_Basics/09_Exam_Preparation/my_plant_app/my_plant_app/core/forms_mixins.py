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
