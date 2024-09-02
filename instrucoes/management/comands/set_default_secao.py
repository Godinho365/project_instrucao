from django.core.management.base import BaseCommand
from secoes.models import Secao
from instrucoes.models import Instrucao

class Command(BaseCommand):
    help = 'Cria uma seção padrão e atualiza instruções sem seção para usar a seção padrão'

    def handle(self, *args, **options):
        # Crie ou obtenha uma seção padrão
        secao_default, created = Secao.objects.get_or_create(nome="Padrão")

        # Atualize instruções sem seção para usar a seção padrão
        Instrucao.objects.filter(secao__isnull=True).update(secao=secao_default)

        self.stdout.write(self.style.SUCCESS('Seção padrão criada e instruções atualizadas com sucesso.'))
