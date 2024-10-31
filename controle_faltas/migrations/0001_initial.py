# Generated by Django 4.1 on 2024-10-29 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CargaFaltas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga_horaria', models.PositiveIntegerField(verbose_name='Carga Horária')),
                ('quantidade_faltas', models.PositiveIntegerField(verbose_name='Quantidade de Faltas')),
            ],
        ),
    ]
