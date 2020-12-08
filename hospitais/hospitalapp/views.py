from django.shortcuts import render
from django.http import HttpResponse
from .forms import Hospitalform
# Create your views here.

def index(request):
    #return HttpResponse("<h1>Aqui é o index<h1>")
    return render(request, 'hospitais/index.html')
def hospitais(request):
    #return HttpResponse("<h1>Aqui é a área de Hospital<h1>")
    return render (request, "hospitais/hospitais.html")

def criar_hospital (request):
    form = Hospitalform(request.POST)
    if form.is_valid():
        hosp = form.save()
        hosp.save()
        form = Hospitalform()
    return render(request, "hospitais/criar_hospitais.html", {'form':form})
