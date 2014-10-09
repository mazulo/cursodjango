# -*- coding: utf-8 -*-
from django.shortcuts import render


def index(request):
    return render(request, 'aula6/index.html')
