from django.db import models

class Secao(models.Model):
    id = models.AutoField(primary_key=True)  # Define explicitamente o campo `id` como um AutoField
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
