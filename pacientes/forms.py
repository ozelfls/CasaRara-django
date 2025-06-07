from django import forms
from .models import Beneficiario, Medico

class BeneficiarioForm(forms.ModelForm):
    class Meta:
        model = Beneficiario
        fields = [
            'Nome',
            'CPF',
            'Data_Nascimento',
            'Endereco',
            'Telefone',
            'Email'
        ]
        widgets = {
            'Data_Nascimento': forms.DateInput(attrs={'type': 'date'}),
            'Endereco': forms.Textarea(attrs={'rows': 3}),
        }

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = [
            'nome',
            'crm',
            'especialidade',
            'cpf',
            'email',
            'telefone'
        ]
        widgets = {
            'crm': forms.TextInput(attrs={'placeholder': 'Digite o CRM'}),
            'especialidade': forms.TextInput(attrs={'placeholder': 'Ex: Pediatria'}),
        }
