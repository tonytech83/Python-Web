from django import forms


class PersonForm(forms.Form):
    """
    Each field has custom validation logic
    Each filed takes some common arguments
    Some fields take field-specific arguments
    """
    OCCUPANCIES = (
        (1, 'Child'),
        (2, 'Student'),
        (3, 'Adult'),
    )

    your_name = forms.CharField(
        max_length=30,
        label='Name',
        help_text='Enter your name here',
        widget=forms.TextInput(
            # This corresponds to HTML attributes
            attrs={
                'placeholder': 'Enter name',
                'class': 'form-control',
            }
        )
    )

    age = forms.IntegerField(
        required=False,
        label='Your age',
        initial=0,
        help_text='Enter your age here',
        widget=forms.NumberInput(),  # This is the default for `IntegerField`
    )

    url = forms.CharField(
        widget=forms.URLInput(),
    )

    secret = forms.CharField(
        widget=forms.PasswordInput(),
    )

    email = forms.CharField(
        widget=forms.EmailInput(),
    )

    occupancy = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.Select,  # This is the default for `ChoiceField`
    )

    occupancy2 = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.RadioSelect(),
    )

    occupancy3 = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.SelectMultiple(),
    )

    story = forms.CharField(
        widget=forms.Textarea(),
    )
