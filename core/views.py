from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

#def index(request):
#    return redirect('/agenda/')

def lista_eventos(request):
    usuario = request.user
    #evento = Evento.objects.get(id=1)
    evento = Evento.objects.all()
    #evento = Evento.objects.filter(usuario=usuario)
    data = {'eventos':evento}
    return render(request, 'agenda.html', data)
