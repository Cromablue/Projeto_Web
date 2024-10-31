# controle_faltas/forms.py
from django import forms

class FaltasForm(forms.Form):
    total_faltas = forms.IntegerField(label="Total de Faltas")
    carga_horaria = forms.IntegerField(label="Carga Horária do Curso")
