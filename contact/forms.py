from django.core.exceptions import ValidationError
from django import forms

from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Aqui veio do init',
        # })
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email',
        )
        """
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'alguma classe',
                    'placeholder': ' Nome ',
                    'label': 'Primeiro nome',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'alguma classe 2',
                    'placeholder': 'Sobrenome',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'alguma classe 3',
                    'placeholder': 'telefone',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'alguma classe 4',
                    'placeholder': 'Email',
                }
            )
        }
"""

    def clean(self):
        #cleaned_data = self.cleaned_data

        self.add_error(
            None, ValidationError(
                'mensagem de erro', code='invalid'
            )
        )

        return super().clean()