from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/novo/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('entregas/nova/', views.nova_entrega, name='nova_entrega'),
    path('entregas/', views.lista_entregas, name='lista_entregas'),
    path('entregas/concluir/<int:id>/', views.concluir_entrega, name='concluir_entrega'),
    path('entregas/devolucao/<int:id>/', views.registrar_devolucao, name='registrar_devolucao'),
     path('', views.lista_entregas, name='home'),  # 👈 ESSA LINHA
   
]