# Generated by Django 4.0.2 on 2022-04-04 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='cancelado',
            field=models.BooleanField(default=False),
        ),
    ]
