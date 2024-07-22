from django.conf.urls import url

from . import views
 
urlpatterns= [
    url(r'^$', views.index, name='index'),
    url(r'^configurarPuerto/', views.configurarPuerto, name='configurarPuerto'),
    url(r'^imprimirReporteX/', views.imprimirReporteX, name='imprimirReporteX')
]