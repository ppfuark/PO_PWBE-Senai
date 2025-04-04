from django.urls import path
from . import views  # Importando views do mesmo diretório

urlpatterns = [
    path('', views.lista_postagens, name='lista_postagens'),  # Ajuste conforme suas views
]
