# secoes/forms.py
from django import forms
from .models import Secao

class SecaoForm(forms.ModelForm):
    class Meta:
        model = Secao
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome da seção'}),
        }
