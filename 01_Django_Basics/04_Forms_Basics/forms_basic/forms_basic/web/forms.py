from django import forms

from forms_basic.web.models import Employee


# Django Form -> not attached to model
class DemoForm(forms.Form):
    MAX_LENGTH_NAME = 35
    INTERESTS = (
        (1, 'Senior'),
        (2, 'Professional'),
        (3, 'Master'),
    )

    first_name = forms.CharField(
        max_length=MAX_LENGTH_NAME,
        required=True,
        label='First Name',
        help_text="Enter your first name.",
        initial='Anonymous',

        # widget takes care of visualization and data gathering

    )

    last_name = forms.CharField(
        max_length=MAX_LENGTH_NAME,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your last name.'
            }
        )
    )

    email = forms.EmailField(
        # change the behaviour of field
        # widget=forms.PasswordInput()
    )

    interests = forms.ChoiceField(
        choices=INTERESTS,
        required=True,
    )

    interests_two = forms.IntegerField(
        # when we use `IntegerFiled` and changed the behavior to `Select`, we kept the key as `integer`
        # when we use `ChoiceField`, the key passes to `string`

        widget=forms.Select(
            choices=INTERESTS
        ),
        required=True,
    )

    interests_three = forms.IntegerField(
        widget=forms.RadioSelect(
            choices=INTERESTS,
        )
    )

    age = forms.IntegerField()


# Django ModelForm -> attached to model
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
