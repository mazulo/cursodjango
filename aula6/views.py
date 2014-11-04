# -*- coding: utf-8 -*-
from django.shortcuts import render
from aula6.models import Contato
from aula6.forms import ContatoForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'aula6/contacts_list.html', {
        'contatos': contatos
    })


def add_contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            novo_contato = Contato(
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email'),
                twitter=form.cleaned_data.get('twitter')
            )
            novo_contato.save()
            return HttpResponseRedirect(reverse('aula6_index'))
    else:
        form = ContatoForm()
    return render(request, 'aula6/add_contato.html', {
        'form': form
    })
