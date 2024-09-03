from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.contrib import messages
from .models import Produto
from . import utils
from . import forms


def catalogo(request):
    return render(request, 'catalogo.html')


def estoque(request):
    form = forms.ProductForm()
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto adicionado com sucesso.")

    busca = utils.construir_busca(request, ['codigo', 'nome'])
    produtos = (
        Produto.objects
        .filter(busca)              # Realizar a busca
        .order_by('-criado_em')     # Ordenar pelo último criado
    )

    return render(request, 'estoque.html', {'produtos': produtos, 'form': form})


def deletar_produto(request, pk=None):
    if request.method == 'POST':
        print(f'Desejo deletar o produto {pk}')
    return redirect('home')


def vendas(request):
    return render(request, 'vendas.html')


def relatorios(request):
    return render(request, 'relatorios.html')
