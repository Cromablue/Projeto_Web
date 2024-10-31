# controle_faltas/models.py
from django.db import models

class CargaFaltas(models.Model):
    carga_horaria = models.PositiveIntegerField("Carga Horária")
    quantidade_faltas = models.PositiveIntegerField("Quantidade de Faltas")

    def faltas_maximas(self):
        return self.carga_horaria // 4

    def verificar_faltas(self):
        if self.quantidade_faltas <= self.faltas_maximas() - 3:
            return "{% static 'assets/imagens/faltemeufilho.png' %} "
        else:
            return "{% static 'assets/imagens/podenaoman.png' %} "
