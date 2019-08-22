from django.http import Http404
from django.shortcuts import render, redirect, resolve_url as r, render_to_response
from core.models import pessoa


def Home(request):
    pess = pessoa.objects.get(id=1)
    return render(request, 'index.html', {'pessoas': pess})

def Login(request):
        pessoas = ({
            'nome':'maycon',
            'sobrenome':'porto dos santos',
            'cpf':'12345678909',
            'dataNasc':'03/19/1998',
            'endereço':'rua 1',
            'telefone':'992208988',
        },{
            'nome':'ricardo',
            'sobrenome':'sousa pimentel',
            'cpf':'12345678909',
            'dataNasc':'03/19/1998',
            'endereço':'rua 1',
            'telefone':'992208988',
        })

        return render(request, 'login.html', {'pessoas': pessoas})
