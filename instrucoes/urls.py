from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.listar_instrucoes, name='listar_instrucoes'),
    path('adicionar/', views.adicionar_instrucao, name='adicionar_instrucao'),
    path('editar/<int:pk>/', views.editar_instrucao, name='editar_instrucao'),
    path('deletar/<int:pk>/', views.deletar_instrucao, name='deletar_instrucao'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
