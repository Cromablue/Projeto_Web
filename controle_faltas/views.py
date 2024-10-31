# controle_faltas/views.py
from django.shortcuts import render
from .forms import FaltasForm

def verificar_faltas(request):
    resultado_imagem = None
    error_message = None
    console_message = ""

    if request.method == "POST":
        form = FaltasForm(request.POST)
        if form.is_valid():
            total_faltas = form.cleaned_data['total_faltas']
            carga_horaria = form.cleaned_data['carga_horaria']

            total_aulas = carga_horaria
            max_faltas = total_aulas / 4

            if (total_faltas > (max_faltas - 3)) and (total_faltas < max_faltas):
                resultado_imagem = '/assets/imagens/podenaoman.png'
                console_message = "Ja era man, pode nao!"
            elif total_faltas >= max_faltas:
                resultado_imagem = '/assets/imagens/reprovouvei.jpg'
                console_message = "Faltou mais que o permitido"
            else:
                resultado_imagem = '/assets/imagens/faltemeufilho.png'
                console_message = "Pode Faltar Man."
        else:
            error_message = "Por favor, insira valores numéricos válidos."
    else:
        form = FaltasForm()

    return render(request, 'controle_faltas/verificar_faltas.html', {
        'form': form,
        'resultado_imagem': resultado_imagem,
        'error_message': error_message,
        'console_message': console_message,
    })
