from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Escolha, Pergunta

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'enquetes/index.html'
    context_object_name = 'lista_ultimas_perguntas'

    def get_queryset(self):
        """Return the last five published questions."""
        return Pergunta.objects.order_by('-data_pub')[:5]

class DetalheView(generic.DetailView):
    model = Pergunta
    template_name = 'enquetes/detalhe.html'

class ResultadosView(generic.DetailView):
    model = Pergunta
    template_name = 'enquetes/resultados.html'

def voto(request, id_pergunta):
	pergunta = get_object_or_404(Pergunta, pk=id_pergunta)
	try:
		selected_choice = pergunta.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'enquetes/detalhe.html', {
			'pergunta': pergunta,
			'error_message': 'Você não selecionou uma opção.',
			})
	else:
		selected_choice.votos += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('enquetes:resultados', args=(id.pergunta,)))
