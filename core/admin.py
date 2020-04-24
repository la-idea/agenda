from django.contrib import admin
from core.models import Evento
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_event', 'hora_criacao')
    list_filter = ('usuario', 'titulo', 'data_event',)
# Essa classe diz o que vai ser mostrado no display do django no navegador, porém ela tem que ser associada no register abaixo

admin.site.register(Evento, EventoAdmin)


