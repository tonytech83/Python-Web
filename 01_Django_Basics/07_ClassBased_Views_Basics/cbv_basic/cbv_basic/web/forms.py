from django import forms

from cbv_basic.web.models import Todo


class TodoBaseForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

    # def clean_title(self):
    #     pass
    #
    # def save(self, commit=True):
    #     pass
