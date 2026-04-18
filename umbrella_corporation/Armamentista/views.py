from django.shortcuts import render

def index_legal(request):
    return render(request, 'armamentista_legal.html')
    
def index_ilegal(request):   
    return render(request, 'AramamentistaIlegal.html')
