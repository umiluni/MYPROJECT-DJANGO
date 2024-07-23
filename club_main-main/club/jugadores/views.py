from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Jugador
from .forms import JugadorForm


# Create your views here

def lista(request):
    jugadores=Jugador.objects.all()
    return render(request,"crud/listado.html",{'jugadores':jugadores})

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')      


def inicio(request):
    return render(request,'paginas_base/inicio.html')        

def crear_editar(request,id=0):
      if request.method=="GET":
        if id==0:
            formulario=JugadorForm()   
        else:
            jugadorid=Jugador.objects.get(pk=id)
            formulario=JugadorForm(instance=jugadorid)
        return render(request,'Crud/crear.html',{'formulario':formulario})
      else:
        if id==0:
            formulario=JugadorForm(request.POST or None, request.FILES or None)
        else:
            jugadorid=Jugador.objects.get(pk=id)
            formulario=JugadorForm(request.POST or None, request.FILES or None ,instance=jugadorid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('lista')
        
def eliminar(request, id):
    bc=Jugador.objects.get(id=id)
    bc.delete()
    return redirect('lista')
        