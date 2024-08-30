from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'Blog/index.html')


def sobre(request): 
    cursos=Cursos.objects.all()
    habilidades=Habilidade.objects.all()
    context={
        'cursos':cursos,
        'habilidades':habilidades
    }
    return render(request, 'Blog/sobre.html',context)