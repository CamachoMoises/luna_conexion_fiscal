from django.conf.urls import url

from . import views
 
urlpatterns= [
    url(r'^$', views.index, name='index'),
    url(r'^configurarPuerto/', views.configurarPuerto, name='configurarPuerto'),
    url(r'^imprimirReporteX/', views.imprimirReporteX, name='imprimirReporteX'),
    url(r'^getReporteX1/', views.getReporteX1, name='getReporteX1'),
    url(r'^getReporteX2/', views.getReporteX2, name='getReporteX2'),
    url(r'^getReporteX4/', views.getReporteX4, name='getReporteX4'),
    url(r'^getReporteX5/', views.getReporteX5, name='getReporteX5'),
    url(r'^getReporteX7/', views.getReporteX7, name='getReporteX7'),
]