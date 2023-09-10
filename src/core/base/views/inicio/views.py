from django.shortcuts import render

def Inicio(request):
    data = {
        'title': 'Inicio',
    }
    return render(request, 'inicio/inicio.html', data)