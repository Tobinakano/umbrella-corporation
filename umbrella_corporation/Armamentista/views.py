from django.shortcuts import render

def index(request):
    return render(request, 'armamentista_legal.html')
