from datetime import date
import requests
from django.conf import settings


def is_feriado(data: date):
    if settings.TESTING == True:
        if date.day == 25 and date.month == 12:
            return True
        return False

    ano = data.year
    req = requests.get(f"https://brasilapi.com.br/api/feriados/v1/{ano}")
    if req.status_code != 200:
        raise ValueError("Não foi possível consultar os feriados")
    feriados = req.json()
    for feriado in feriados:
        data_feriado_str = feriado["date"]
        data_feriado = date.fromisoformat(data_feriado_str)
        if data == data_feriado:
            return True
    return False
