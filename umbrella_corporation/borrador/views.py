from django.shortcuts import render

def index_view(request):
	return render(request, 'index.html')

def empresa_view(request):
	return render(request, 'empresa.html')

def investigacion_view(request):
	return render(request, 'investigacion.html')

def ubicaciones_view(request):
	return render(request, 'ubicaciones.html')
