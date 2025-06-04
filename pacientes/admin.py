from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Beneficiario

@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = ('ID_Beneficiario', 'Nome', 'CPF', 'Email', 'Data_Cadastro')
    search_fields = ('Nome', 'CPF', 'Email')
    list_filter = ('Data_Cadastro',)
    readonly_fields = ('ID_Beneficiario', 'Data_Cadastro')
    date_hierarchy = 'Data_Cadastro'