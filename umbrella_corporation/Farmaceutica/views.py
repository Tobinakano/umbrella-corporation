from django.shortcuts import render

def index_farmaceutica(request):
    return render(request, 'index_farmacia.html')