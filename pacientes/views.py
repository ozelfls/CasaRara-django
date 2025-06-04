# pacientes/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['casaRara']
pacientes_collection = db['pacientes']

def cadastrar_paciente(request):
    if request.method == 'POST':
        try:
            dados = {
                "Nome": request.POST.get('nome', '').strip(),
                "CPF": request.POST.get('cpf', '').strip(),
                "Data_Nascimento": datetime.strptime(request.POST.get('dataNascimento'), '%Y-%m-%d'),
                "Endereco": request.POST.get('endereco', '').strip(),
                "Telefone": request.POST.get('telefone', '').strip(),
                "Email": request.POST.get('email', '').strip(),
                "Sexo": request.POST.get('sexo', '').strip(),
                "Data_Cadastro": datetime.utcnow()
            }
            pacientes_collection.insert_one(dados)
            return redirect('sucesso')
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar: {str(e)}')
    return render(request, 'pacientes/cadastro_paciente.html')

def sucesso_view(request):
    return render(request, 'pacientes/sucesso.html')





from django.shortcuts import render, redirect
from .forms import MedicoForm
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["casaRara"]
colecao_medicos = db["medicos"]

def cadastrar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            dados['_id'] = str(ObjectId())
            colecao_medicos.insert_one(dados)
            return render(request, 'pacientes/sucesso.html')
    else:
        form = MedicoForm()
    return render(request, 'pacientes/medico.html', {'form': form})
