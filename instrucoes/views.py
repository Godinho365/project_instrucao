from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Instrucao, Secao
from .forms import InstrucaoForm

def listar_instrucoes(request):
    instrucoes = Instrucao.objects.all()
    return render(request, 'instrucoes/lista.html', {'instrucoes': instrucoes})

def adicionar_instrucao(request):
    if request.method == 'POST':
        form = InstrucaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Instrução adicionada com sucesso.')
            return redirect('listar_instrucoes')
        else:
            messages.error(request, 'Erro ao adicionar a instrução. Por favor, corrija os erros abaixo.')
    else:
        form = InstrucaoForm()

    return render(request, 'instrucoes/adicionar.html', {'form': form})

def editar_instrucao(request, pk):
    instrucao = get_object_or_404(Instrucao, pk=pk)
    
    if request.method == 'POST':
        form = InstrucaoForm(request.POST, request.FILES, instance=instrucao)
        
        # Lógica para remover imagem se necessário
        if 'remover_imagem' in request.POST and instrucao.imagem:
            instrucao.imagem.delete(save=False)  # Apaga o arquivo de imagem, mas não salva imediatamente o objeto
            instrucao.imagem = None
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Instrução editada com sucesso.')
            return redirect('listar_instrucoes')
        else:
            messages.error(request, 'Erro ao editar a instrução. Por favor, corrija os erros abaixo.')
    else:
        form = InstrucaoForm(instance=instrucao)
    
    return render(request, 'instrucoes/editar.html', {'form': form, 'instrucao': instrucao})

def deletar_instrucao(request, pk):
    instrucao = get_object_or_404(Instrucao, pk=pk)
    if request.method == 'POST':
        instrucao.delete()
        messages.success(request, 'Instrução deletada com sucesso.')
        return redirect('listar_instrucoes')
    return render(request, 'instrucoes/deletar.html', {'instrucao': instrucao})
