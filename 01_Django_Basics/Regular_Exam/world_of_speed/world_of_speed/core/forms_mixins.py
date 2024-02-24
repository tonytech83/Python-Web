class SetPlaceholderMixin:
    placeholders = {}

    def set_placeholders(self):
        for field_name in self.placeholders:
            self.fields[field_name].widget.attrs['placeholder'] = self.placeholders[field_name]


class ReadOnlyFieldsFormMixin:
    readonly_fields = ()

    def apply_readonly_fields(self):
        for field_name in self.readonly_fields:
            self.fields[field_name].widget.attrs['readonly'] = True


class HideHelpTextFormMixin:
    help_text_fields = ()

    def hide_help_text_fields(self):
        for field_name in self.help_text_fields:
            self.fields[field_name].help_text = None
