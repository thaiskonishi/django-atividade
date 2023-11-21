from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'homepage/index.html')

#colocar sempre primeiro o request e depois o srquivo que quero renderizar
def cadastro(request):
    return render(request,'homepage/cadastro.html')

def produtos(request):
    return render(request,'homepage/produtos.html')