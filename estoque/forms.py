from django.core.exceptions import ValidationError
from django import forms
from .models import Produto

class ProductForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"

    def clean_nome(self):
        print('clean nome')
        nome = self.cleaned_data['nome']
        if nome == 'cocaina':
            raise ValidationError('Cocaína não é permitido')
        return nome