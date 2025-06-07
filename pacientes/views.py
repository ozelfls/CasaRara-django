# pacientes/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Beneficiario, Medico
from .forms import MedicoForm
from datetime import datetime

def cadastrar_paciente(request):
    if request.method == 'POST':
        try:
            beneficiario = Beneficiario(
                Nome=request.POST.get('nome', '').strip(),
                CPF=request.POST.get('cpf', '').strip(),
                Data_Nascimento=datetime.strptime(request.POST.get('dataNascimento'), '%Y-%m-%d'),
                Endereco=request.POST.get('endereco', '').strip(),
                Telefone=request.POST.get('telefone', '').strip(),
                Email=request.POST.get('email', '').strip()
            )
            beneficiario.save()
            return redirect('sucesso')
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar: {str(e)}')
    return render(request, 'pacientes/cadastro_paciente.html')


def cadastrar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
        else:
            messages.error(request, 'Erro no formulário.')
    else:
        form = MedicoForm()
    return render(request, 'pacientes/medico.html', {'form': form})


def sucesso_view(request):
    return render(request, 'pacientes/sucesso.html')
