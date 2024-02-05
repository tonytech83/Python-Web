from django import forms


class EmployeeForm(forms.Form):
    MAX_LENGTH_NAME = 35

    first_name = forms.CharField(
        max_length=MAX_LENGTH_NAME,
        required=True,
    )

    last_name = forms.CharField(
        max_length=MAX_LENGTH_NAME,
        required=True,
    )
