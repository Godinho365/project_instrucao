# secoes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Secao
from instrucoes.models import Instrucao  # Corrigido para importar do módulo correto
from .forms import SecaoForm

def listar_secoes(request):
    secoes = Secao.objects.all()
    return render(request, 'secoes/lista.html', {'secoes': secoes})

def adicionar_secao(request):
    if request.method == 'POST':
        form = SecaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_secoes')
    else:
        form = SecaoForm()
    return render(request, 'secoes/adicionar.html', {'form': form})

def editar_secao(request, pk):
    secao = get_object_or_404(Secao, pk=pk)
    if request.method == 'POST':
        form = SecaoForm(request.POST, instance=secao)
        if form.is_valid():
            form.save()
            return redirect('listar_secoes')
    else:
        form = SecaoForm(instance=secao)
    return render(request, 'secoes/editar.html', {'form': form, 'secao': secao})

def deletar_secao(request, pk):
    secao = get_object_or_404(Secao, pk=pk)
    if request.method == 'POST':
        secao.delete()
        return redirect('listar_secoes')
    return render(request, 'secoes/deletar.html', {'secao': secao})

def listar_instrucoes_por_secao(request, secao_id):
    secao = get_object_or_404(Secao, id=secao_id)
    instrucoes = Instrucao.objects.filter(secao=secao)
    return render(request, 'secoes/lista_instrucoes_por_secao.html', {'secao': secao, 'instrucoes': instrucoes})
