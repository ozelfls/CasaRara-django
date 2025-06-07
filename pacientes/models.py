from django.db import models
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

class Medico(models.Model):
    nome = models.CharField(max_length=255)
    crm = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=100)
    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            MinLengthValidator(11),
            RegexValidator(r'^\d{11}$', 'CPF deve conter apenas números')
        ]
    )
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
        ordering = ['-data_cadastro']

    def __str__(self):
        return f"{self.nome} (CRM: {self.crm})"
