from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_event = models.DateTimeField()
    hora_criacao = models.DateTimeField(auto_now=True)
    # Parâmetro auto_now faz a variável receber a hora de criação do objeto
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'evento'

# Meta dados da classe setam parâmetros na migração para o banco de dados
    def __str__(self):
        return self.titulo
# Traz o nome do título do evento como nome do objeto


    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y')
# Posso colocar uma função aqui no models e chamar no meu html através do objeto

   # def get_data_input_evento(self):
    #    return self.data_event.strftime('%Y-%m-%dT%H:%M')
