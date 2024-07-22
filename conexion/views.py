# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from utilidades.impresora import testF, configurarPueto, ReporteXPrint,datosReporteX1, datosReporteX2, datosReporteX4, datosReporteX5, datosReporteX7
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
    
def getReporteX1(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosReporteX1(PORT)
            return JsonResponse({"mensaje":"Datos del reporte X1", "datos":datos.__dict__}) 
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta") 
    
def getReporteX2(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosReporteX2(PORT)
            return JsonResponse({"mensaje":"Datos del reporte X2", "datos":datos.__dict__}) 
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta") 
    
    
def getReporteX4(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosReporteX4(PORT)
            return JsonResponse({"mensaje":"Datos del reporte X4", "datos":datos.__dict__}) 
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta") 
    
def getReporteX5(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosReporteX5(PORT)
            return JsonResponse({"mensaje":"Datos del reporte X5", "datos":datos.__dict__}) 
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta") 
    
def getReporteX7(req):
    PORT = cache.get('PORT')
    DB_PORT = Puerto.objects.last()
    
    print(PORT)
    try:
        if PORT == DB_PORT.nombre and isinstance(PORT,str):
            datos=datosReporteX7(PORT)
            return JsonResponse({"mensaje":"Datos del reporte X7", "datos":datos.__dict__}) 
        else:
            raise Exception("los tipos con coinciden")

    except Exception as e:
        print(e)
        return HttpResponse("Error de consulta") 
        
        
        



    

