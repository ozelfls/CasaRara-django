from django.contrib import admin
from django.urls import path, include
from paginas import views as paginas_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pacientes.urls')),
    path('', paginas_views.index_view, name='index'),
    path('about/', paginas_views.about_view, name='about'),
    path('inicio/', paginas_views.index_view),
    path('connect/', paginas_views.connect_view, name='connect'),
    path('sobre/', paginas_views.about_view),
    path('pacient/', paginas_views.pacient_view, name='paciente'),
    path('volunt/', paginas_views.volunt_view, name='volunt'),
    path('unidade/', paginas_views.unidade_view, name='unidade'),
]
