# Generated by Django 4.0.3 on 2022-03-15 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_evento_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='participantes',
            field=models.IntegerField(default=0),
        ),
    ]
