from django.shortcuts import render,redirect,get_object_or_404

from .models import gato

# Create your views here.

def index(request):
    contexto = {}
    return render(request, 'index.html', contexto)

def perros(request):
    contexto = {}
    return render(request, 'perros.html', contexto)

def gatos(request):
    gatos = gato.objects.all()
    contexto = {'gatos': gatos}
    return render(request, 'gatos.html', contexto)

def contact(request):
    contexto = {}
    return render(request, 'contact.html', contexto)

def login(request):
    contexto = {}
    return render(request, 'login.html', contexto)

def pcausa(request):
    contexto = {}
    return render(request, 'perros/pcausa.html', contexto)

def pcopito(request):
    contexto = {}
    return render(request, 'perros/pcopito.html', contexto)

def pmatapaco(request):
    contexto = {}
    return render(request, 'perros/pmatapaco.html', contexto)

def gefigen(request):
    contexto = {}
    return render(request, 'gatos/gefigen.html', contexto)

def ggrunon(request):
    contexto = {}
    return render(request, 'gatos/ggrunon.html', contexto)

def gpelusa(request):
    contexto = {}
    return render(request, 'gatos/gpelusa.html', contexto)

def crud(request):
    gatos = gato.objects.all()
    contexto = {'gatos': gatos}
    return render(request, 'crud/mostrar.html', contexto)

def agregar_gato(request):
    if request.method == 'POST':
        cod_gato = request.POST.get('cod_gato')
        nombre_gato = request.POST.get('nombre_gato')
        edad_gato = request.POST.get('edad_gato')
        raza_gato = request.POST.get('raza_gato')
        esterelizacion_gato = request.POST.get('esterelizacion_gato') == 'true' 
        fecha_nac = request.POST.get('fecha_nac')

        nuevo_gato = gato(cod_gato=cod_gato, nombre_gato=nombre_gato, edad_gato=edad_gato, raza_gato=raza_gato, esterelizacion_gato=esterelizacion_gato, fecha_nac=fecha_nac)
        nuevo_gato.save()

        return redirect('agregar')

    return render(request, 'crud/agregar.html')

def eliminar_gato(request, cod_gato):
    gato_a_eliminar = get_object_or_404(gato, cod_gato=cod_gato)
    gato_a_eliminar.delete()

    return redirect('mostrar')

def modificar_gato(request, cod_gato):
    gato_a_modificar = get_object_or_404(gato, cod_gato=cod_gato)

    if request.method == 'POST':
        nombre_gato = request.POST.get('nombre_gato')
        edad_gato = request.POST.get('edad_gato')
        raza_gato = request.POST.get('raza_gato')
        esterelizacion_gato = request.POST.get('esterelizacion_gato') == 'true'
        fecha_nac = request.POST.get('fecha_nac')

        gato_a_modificar.nombre_gato = nombre_gato
        gato_a_modificar.edad_gato = edad_gato
        gato_a_modificar.raza_gato = raza_gato
        gato_a_modificar.esterelizacion_gato = esterelizacion_gato
        gato_a_modificar.fecha_nac = fecha_nac

        gato_a_modificar.save()

        return redirect('mostrar')

    return render(request, 'crud/modificar.html', {'gato': gato_a_modificar})