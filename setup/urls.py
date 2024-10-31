# setup/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('controle_faltas.urls')),  # Inclui as URLs do aplicativo controle_faltas
]
