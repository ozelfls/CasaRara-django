from django.shortcuts import render

def index(request):
    return render(request, 'paginas/index.html')

def about_view(request):
    return render(request, 'paginas/about.html')

def connect_view(request):
    return render(request, 'paginas/connect.html')

def pacient_view(request):
    return render(request, 'paginas/pacient.html')

def unidade_view(request):
    return render(request, 'paginas/unidade.html')

def volunt_view(request):
    return render(request, 'paginas/volunt.html')

def sucesso_view(request):
    return render(request, 'pacientes/sucesso.html')

from django.shortcuts import render

def index_view(request):
    return render(request, 'paginas/index.html')

def connect_view(request):
    return render(request, 'paginas/connect.html')

from django.shortcuts import render
from django.http import HttpResponse
def submit(request):
    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        return HttpResponse(f"Dados recebidos: {nome}, {email}")
    return HttpResponse("Método inválido", status=405)


