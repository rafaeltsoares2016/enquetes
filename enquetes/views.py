from django.shortcuts import render
from django.http import HttpResponse

from .models import Pergunta

# Create your views here.

def index(request):
	lista_ultimas_perguntas = Pergunta.objects.order_by('-data_pub')[:5]
	template = loader.get_template('enquetes/index.html')
	context = {
		'lista_ultimas_perguntas':lista_ultimas_perguntas,
	}
	return HttpResponse(template.render(context, request))

def detalhe(request, id_pergunta):
	return HttpResponse('Você esta olhando a pegunta %s.' % id_pergunta)

def resultados(request, id_pergunta):
	response = 'Você esta olhando os resultados da pergunta %s.'
	return HttpResponse(response % id_pergunta)

def voto(request, id_pergunta):
	return HttpResponse('Você esta votando na pergunta %s.' % id_pergunta)
