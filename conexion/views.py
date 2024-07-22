# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from utilidades.impresora import testF, configurarPueto, ReporteXPrint
from django.core.cache import cache
from models import Puerto

# Create your views here.

def index(request):
    intentos = cache.get_or_set('intentos', 0)
    intentos += 1
    cache.set('intentos', intentos)
    print('intentos del dia', intentos)
    status=testF()
    return HttpResponse("Hello word")

def configurarPuerto(request):
    DB_PORT=Puerto.objects.last()
    print('Ultimo puerto:' + DB_PORT.nombre)
    PORT = cache.get_or_set('PORT', '')
    PORT = configurarPueto()
    cache.set('PORT', PORT)
    Puerto.objects.create(
        nombre=PORT
    )
    return HttpResponse("puerto configurado: "+ PORT)

def imprimirReporteX(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    if PORT == DB_PORT.nombre and isinstance(PORT,str):
        ReporteXPrint(PORT)
        return HttpResponse("Reporte Impreso")
    else:
        return HttpResponse("error al imprimir")

        
        



    

