from django import forms


class DisabledFormMixin:
    """
    With this mixin we can dynamically disable fields.
    In our form we should pass `disabled_fields`, which we do not want to be editable.
    """
    disabled_fields = ()
    fields = {}

    def _disabled_fields(self):
        if self.disabled_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields

        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs['readonly'] = 'readonly'


class HidedFormMixin:
    """
    With this mixin we can hide all fields in form.
    """
    fields = {}

    def _hide_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()
