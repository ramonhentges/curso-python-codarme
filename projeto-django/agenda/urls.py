from django.urls import path
from agenda.views import index, exibir_evento

urlpatterns = [
    path('', index),
    path('evento', exibir_evento)
]
