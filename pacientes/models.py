from djongo import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, RegexValidator
import random

def gerar_id_unico():
    return random.randint(100000, 999999)

class Beneficiario(models.Model):
    ID_Beneficiario = models.IntegerField(
        default=gerar_id_unico,
        verbose_name="ID do Beneficiário",
        unique=True,
        editable=False,
    )
    Nome = models.CharField(
        max_length=255,
        verbose_name="Nome Completo",
        validators=[MinLengthValidator(3)]
    )
    CPF = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="CPF",
        validators=[
            MinLengthValidator(11),
            RegexValidator(r'^\d{11}$', 'CPF deve conter apenas números')
        ]
    )
    Data_Nascimento = models.DateField(
        verbose_name="Data de Nascimento"
    )
    Endereco = models.TextField(
        verbose_name="Endereço Completo"
    )
    Telefone = models.CharField(
        max_length=20,
        verbose_name="Telefone",
    )
    Email = models.EmailField(
        verbose_name="E-mail"
    )
    Data_Cadastro = models.DateTimeField(
        default=timezone.now,
        verbose_name="Data de Cadastro",
        editable=False,
    )

class Medico:
    def __init__(self, nome, crm, especialidade, cpf, email, telefone):
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['-Data_Cadastro']

    def __str__(self):
        return f"{self.Nome} (CPF: {self.CPF})"
