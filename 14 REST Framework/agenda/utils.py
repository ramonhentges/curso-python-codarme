from datetime import datetime
from datetime import datetime, timezone


def entre_horario_trabalho(horario_verificacao, data):
    data_hora_inicial_manha = datetime(
        data.year, data.month, data.day,  hour=9, minute=0, second=0, tzinfo=timezone.utc)
    if data.weekday() == 5:
        data_hora_final_manha = datetime(
            data.year, data.month, data.day,  hour=12, minute=30, second=0, tzinfo=timezone.utc)
    else:
        data_hora_final_manha = datetime(
            data.year, data.month, data.day,  hour=11, minute=30, second=0, tzinfo=timezone.utc)
    data_hora_inicial_tarde = datetime(
        data.year, data.month, data.day,  hour=13, minute=0, second=0, tzinfo=timezone.utc)
    data_hora_final_tarde = datetime(
        data.year, data.month, data.day,  hour=17, minute=30, second=0, tzinfo=timezone.utc)
    return (horario_verificacao >= data_hora_inicial_manha and horario_verificacao <= data_hora_final_manha) or (horario_verificacao >= data_hora_inicial_tarde and horario_verificacao <= data_hora_final_tarde)


def entre_intervalo(horario_verificacao, data):
    data_hora_final_manha = datetime(
        data.year, data.month, data.day,  hour=11, minute=30, second=0, tzinfo=timezone.utc)
    data_hora_inicial_tarde = datetime(
        data.year, data.month, data.day,  hour=13, minute=0, second=0, tzinfo=timezone.utc)
    return horario_verificacao > data_hora_final_manha and horario_verificacao < data_hora_inicial_tarde
