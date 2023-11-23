from django.shortcuts import render
from homepage.models import Fotografia

# Create your views here.
def index(request):
    fotografias = Fotografia.objects.all()
    
    return render(request,'homepage/index.html',{"cards": fotografias})

#colocar sempre primeiro o request e depois o srquivo que quero renderizar
def cadastro(request):
    return render(request,'homepage/cadastro.html')

def produtos(request):
    return render(request,'homepage/produtos.html')
