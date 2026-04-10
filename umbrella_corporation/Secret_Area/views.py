from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def landing(request):
    return render(request, 'landing.html')

def empresa(request):
    return render(request, 'empresa.html')

def investigacion(request):
    return render(request, 'investigacion.html')

def ubicaciones(request):
    return render(request, 'ubicaciones.html')
