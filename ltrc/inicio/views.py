# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def inicio(request, id=None):
    # return render(request, 'w2r.html', {'id':id})
    return render(request, 'inicio.html', {})