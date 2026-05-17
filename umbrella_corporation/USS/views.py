from django.shortcuts import render

# Create your views here.

def index_uss(request):
    return render(request, 'index_uss.html')
