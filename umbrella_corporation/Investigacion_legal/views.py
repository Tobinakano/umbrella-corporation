from django.shortcuts import render

# Create your views here.

def index_investigacion_legal(request):
    return render(request, 'index_investigacion_legal.html')
