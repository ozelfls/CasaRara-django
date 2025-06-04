from django import forms

class BeneficiarioForm(forms.Form):
    Nome = forms.CharField(max_length=255)
    CPF = forms.CharField(max_length=11, min_length=11)
    Data_Nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    Endereco = forms.CharField(widget=forms.Textarea)
    Telefone = forms.CharField(max_length=20)
    Email = forms.EmailField(required=False)


class MedicoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    crm = forms.CharField(max_length=20)
    especialidade = forms.CharField(max_length=50)
    cpf = forms.CharField(max_length=14)
    email = forms.EmailField()
    telefone = forms.CharField(max_length=15)
