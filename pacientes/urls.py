from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.cadastrar_paciente, name='submit'),
    path('sucesso/', views.sucesso_view, name='sucesso'),
    path('submit', views.cadastrar_paciente),
    path('cadastrar-medico/', views.cadastrar_medico, name='cadastrar_medico'),
]
