from datetime import timedelta
from django.utils import timezone
from rest_framework import serializers

from agenda.models import Agendamento, entre_horario_trabalho
import re


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ["id", "data_horario", "nome_cliente",
                  "email_cliente", "telefone_cliente"]

    def validate_data_horario(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                "Agendamento não pode ser feito no passado")
        max_datetime = value + timedelta(minutes=30)
        min_datetime = value - timedelta(minutes=30)
        count = Agendamento.objects.filter(cancelado=False).filter(
            data_horario__gt=min_datetime).filter(data_horario__lt=max_datetime).count()
        if count > 0:
            raise serializers.ValidationError(
                "O horário entre atendimentos deve ter 30 minutos de intervalo")
        if not entre_horario_trabalho(value, value.date()):
            raise serializers.ValidationError(
                "Não está dentro do horário de trabalho")
        return value

    def validate_telefone_cliente(self, value: str):
        withoutAllowedChars = re.sub(r"\(?\)?-?\+?", "", value)
        onlyNumbers = re.sub(r"[^0-9]", "", value)
        if len(withoutAllowedChars) < 8:
            raise serializers.ValidationError(
                "Telefone deve ter no mínimo 8 dígitos")
        if len(withoutAllowedChars) != len(onlyNumbers):
            raise serializers.ValidationError(
                "São permitidos apenas números e os caracteres + - ( )")
        if value.find("+", 1) != -1:
            raise serializers.ValidationError(
                "+ só é permitido no início do telefone")
        return value

    def validate(self, attrs):
        telefone_cliente = attrs.get("telefone_cliente", "")
        email_cliente = attrs.get("email_cliente", "")
        data_horario = attrs.get("data_horario", "")
        if email_cliente.endswith(".br") and telefone_cliente.startswith("+") and not telefone_cliente.startswith("+55"):
            raise serializers.ValidationError(
                {'email_cliente': ["E-mail brasileiro deve ter um telefone do Brasil"]})
        data = data_horario.date()
        agendamentos_no_dia = Agendamento.objects.filter(cancelado=False).filter(
            email_cliente=email_cliente).filter(data_horario__date=data).count()
        if agendamentos_no_dia > 0:
            raise serializers.ValidationError(
                {'data_horario': ["Você só pode realizar um agendamento por dia"]})
        return attrs


#    def create(self, validated_data):
#        agendamento = Agendamento.objects.create(
#            data_horario=validated_data["data_horario"],
#            nome_cliente=validated_data["nome_cliente"],
#            email_cliente=validated_data["email_cliente"],
#            telefone_cliente=validated_data["telefone_cliente"],)
#        return agendamento

#    def update(self, instance, validated_data):
#        instance.data_horario = validated_data.get(
#            "data_horario", instance.data_horario)
#        instance.nome_cliente = validated_data.get(
#            "nome_cliente", instance.nome_cliente)
#        instance.email_cliente = validated_data.get(
#            "email_cliente", instance.email_cliente)
#        instance.telefone_cliente = validated_data.get(
#            "telefone_cliente", instance.telefone_cliente)
#        instance.save()
#        return instance
