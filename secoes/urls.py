# secoes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_secoes, name='listar_secoes'),
    path('adicionar/', views.adicionar_secao, name='adicionar_secao'),
    path('editar/<int:pk>/', views.editar_secao, name='editar_secao'),
    path('deletar/<int:pk>/', views.deletar_secao, name='deletar_secao'),
    path('<int:secao_id>/instrucoes/', views.listar_instrucoes_por_secao, name='listar_instrucoes_por_secao'),
]
