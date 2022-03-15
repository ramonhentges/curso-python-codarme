from unicodedata import name
from django.urls import path
from agenda.views import exibir_categoria, listar_categorias, listar_eventos, exibir_evento, participar

urlpatterns = [
    path('', listar_eventos, name='listar_eventos'),
    path('eventos/<int:id>/', exibir_evento, name='exibir_evento'),
    path('participar', participar, name='participar'),
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/<int:id>/', exibir_categoria, name='exibir_categoria'),
]
