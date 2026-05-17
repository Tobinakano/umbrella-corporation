from django.shortcuts import render

# Create your views here.

def index_secret_area(request):
    return render(request, 'index_secret_area.html')

def landing(request):
    return render(request, 'landing.html')

def empresa(request):
    return render(request, 'empresa.html')

def investigacion(request):
    return render(request, 'investigacion.html')

def ubicaciones(request):
    return render(request, 'ubicaciones.html')
