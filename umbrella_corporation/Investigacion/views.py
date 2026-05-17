from django.shortcuts import render
from django.http import HttpResponse

def index_investigacion(request):
    return render(request, 'landing_investigacion.html')