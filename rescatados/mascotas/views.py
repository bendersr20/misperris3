from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona, Comuna, Regiones, Vivienda




# Create your views here.
def index(request):
    return render(request, 'index.html',{})



def registro(request):
    return render(request, "formulario.html", {'nombre': ""})

def crear(request):
    nombre = request.POST.get('nombre','')
    rut = request.POST.get('rut',1)
    email = request.POST.get('email','')
    telefono = request.POST.get('telefono',0)
    fecha = request.POST.get('fecha', '2000-01-01')
    region = request.POST.get('nom_reg','')
    comuna = request.POST.get('nom_comuna','')
    tipo = request.POST.get('tp-vivienda','')
    persona = Persona(nombre=nombre, rut=rut, email=email, comuna=comuna,region=region, fec_nac=fecha, fono=telefono, tp_vivienda= tipo)
    persona.save()
    return render(request, "recibido.html")


def listar(request):
    return render(request, 'listar.html', {'elementos':Persona.objects.all()})


def buscar(request, id):
    postulante = Persona.objects.get(pk=id)
    return HttpResponse('rut:' + str(Persona.rut) + '<br> Nombre :' + Persona.nombre_full  + '<br> email:' + str(Persona.email))


def eliminar(request, id):
    adoptante = Persona.objects.get(pk=id)
    adoptante.delete()
    return render(request, 'listar.html', {'elementos': Persona.objects.all()})


def editar(request, id):
    adoptante =Persona.objects.get(pk=id)
    return render(request, 'editar.html',{'persona': Persona})


def edicion(request, id):
    persona = Persona.objects.get(pk=id)
    nombre = request.POST.get('nombre','')
    email = request.POST.get('email','')
    telefono = request.POST.get('telefono',0)
    fecha = request.POST.get('fecha', '')
    region = request.POST.get('nom_reg','')
    comuna = request.POST.get('nom_comuna','')
    tipo = request.POST.get('tipo_vivienda','')
    adoptante = Persona(nombre_full=nombre, rut=id, email=email, comuna=comuna,region=region, fec_nac=fecha, fono=telefono, tipo_vivienda= tipo)
    adoptante.save()
    return render(request, 'listar.html', {'elementos': Persona.objects.all()})