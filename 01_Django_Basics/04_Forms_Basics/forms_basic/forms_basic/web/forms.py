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

    email = forms.EmailField(
        # change the behaviour of field
        # widget=forms.PasswordInput()
    )

    interests = forms.ChoiceField(
        choices=(
            ('Senior', 'Senior'),
            ('Professional', 'Professional'),
            ('Master', 'Master'),
        ),
    )

    age = forms.IntegerField()
