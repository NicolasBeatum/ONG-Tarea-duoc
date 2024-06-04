from django.shortcuts import render

# Create your views here.

def index(request):
    contexto = {}
    return render(request, 'index.html', contexto)

def perros(request):
    contexto = {}
    return render(request, 'perros.html', contexto)

def gatos(request):
    contexto = {}
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