from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:id_pergunta>/', views.detalhe, name='detalhe'),
	path('<int:id_pergunta>/resultados/', views.resultados, name='resultados'),
	path('<int:id_pergunta>/voto/', views.voto, name='voto'),
]