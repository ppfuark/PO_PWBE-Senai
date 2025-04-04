from django.shortcuts import render
from .models import Product

def lista_produtos(request):
    produtos = Product.objects.all().order_by('-titulo')
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})