# instrucoes_site/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from instrucoes import views  # Adicione esta linha para importar as views do app 'instrucoes'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar_instrucoes, name='home'),  # Define a view de listagem de instruções como página inicial
    path('instrucoes/', include('instrucoes.urls')),
    path('secoes/', include('secoes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
