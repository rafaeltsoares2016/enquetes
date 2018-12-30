from django.db import models

# Create your models here.

class Pergunta(models.Model):
	texto_pergunta = models.CharField(max_length=200)
	data_pub = models.DateTimeField('date published')

	def __str__(self):
		return self.texto_pergunta

class Escolha(models.Model):
	pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
	texto_escolha = models.CharField(max_length=200)
	votos = models.IntegerField(default=0)		
		
	def __str__(self):
		return self.texto_escolha
