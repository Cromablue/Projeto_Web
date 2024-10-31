# controle_faltas/urls.py
from django.urls import path
from controle_faltas.views import verificar_faltas

urlpatterns = [ 
    path('', verificar_faltas, name='controle_faltas'),  # URL para a view de controle de faltas
]
