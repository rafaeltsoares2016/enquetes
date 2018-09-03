from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('Olá, mundo. Você esta no index das enquetes.')