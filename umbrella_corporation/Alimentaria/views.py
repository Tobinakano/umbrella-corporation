from django.shortcuts import render

# Create your views here.

def index_alimentaria(request):
    return render(request, 'alimentaria.html')
