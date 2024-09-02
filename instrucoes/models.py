from django.db import models  
from ckeditor.fields import RichTextField  
from secoes.models import Secao

class Instrucao(models.Model):
    id = models.AutoField(primary_key=True)  # Define explicitamente o campo `id` como AutoField
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='instrucoes_imagens/', blank=True, null=True)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)
    conteudo = RichTextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
