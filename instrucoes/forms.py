from django import forms
from .models import Instrucao, Secao
from ckeditor.widgets import CKEditorWidget  # Importa o widget do CKEditor

class InstrucaoForm(forms.ModelForm):
    conteudo = forms.CharField(widget=CKEditorWidget())  # Usa o CKEditor para o campo de conteúdo

    class Meta:
        model = Instrucao
        fields = ['titulo', 'imagem', 'conteudo', 'secao']  # Incluindo apenas os campos necessários
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o título'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'secao': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        # Remover qualquer argumento extra desnecessário
        super().__init__(*args, **kwargs)
        
        # (Opcional) Caso queira filtrar as opções de seção, poderia fazer algo assim:
        # self.fields['secao'].queryset = Secao.objects.filter(condicao=True)
