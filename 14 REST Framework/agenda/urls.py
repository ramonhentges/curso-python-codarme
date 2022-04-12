from django.urls import path
from agenda.views import AgendamentoDetail, AgendamentoList, horarios_list

urlpatterns = [
    path('agendamentos/', AgendamentoList.as_view()),
    path('agendamentos/<int:id>/', AgendamentoDetail.as_view()),
    path('horarios/', horarios_list),
]
