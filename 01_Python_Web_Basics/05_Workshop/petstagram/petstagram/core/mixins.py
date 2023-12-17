class StrFromFieldMixin:
    str_fields = ()

    def __str__(self):
        return ','.join(
            f'{str_field}={getattr(self, str_field, None)}' for str_field in self.str_fields
        )
