from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect, resolve_url as r, render_to_response
from core.forms import PessoaForm, EquipamentoForm
from core.models import Pessoa, Equipamento


def Home(request):

    equipamentolist = Equipamento.objects.all()

    pess = Pessoa.objects.filter(ativo=True)




    return render(request, 'index.html', {'pessoas': pess, 'equipamentoslista':equipamentolist})

def Login(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'login.html', {'pessoas': pessoas})


def cadastroPessoa(request):
    url = 'cadastroPessoa'
    form = PessoaForm(request)
    if request.method == 'POST':
        # cria uma instancia do formulario de preenchimento dos dados do AD com os dados vindos do request POST:
        form = PessoaForm(request, data=request.POST)
        # Checa se os dados são válidos:
        if form.is_valid():
            form.save()
            #messages.success(request, 'Configurações salvas com sucesso!')


    return render(request, 'cadastros.html', {'formulario': form, 'endereco':url})


def cadastroEquipamento(request):
    url = 'cadastroEquipamento'
    form = EquipamentoForm(request)
    if request.method == 'POST':
        # cria uma instancia do formulario de preenchimento dos dados do AD com os dados vindos do request POST:
        form = EquipamentoForm(request, data=request.POST)
        # Checa se os dados são válidos:
        if form.is_valid():
            form.save()
            messages.success(request, 'Configurações salvas com sucesso!')
            return redirect('cadastroEquipamento')


    return render(request, 'cadastros.html', {'formulario': form, 'endereco':url})