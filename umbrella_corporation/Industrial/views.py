from django.shortcuts import render

# Create your views here.

def index_industrial(request):
    return render(request, 'index_industrial.html')
