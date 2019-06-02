from django.shortcuts import render
from .models import Cliente
from .models import Produtos
from .models import Pedidos





def clientes(request):
    dataclientes = {}
    dataclientes['varclientes'] = Cliente.objects.all()
    return render(request, 'clientes.html', dataclientes)
    


def produtos(request):
    dataprodutos = {}
    dataprodutos['varprodutos'] = Produtos.objects.all()
    return render(request, 'produtos.html', dataprodutos)


def pedidos(request):
    datapedidos = {}
    datapedidos['varpedidos'] = Pedidos.objects.all()
    return render(request, 'pedidos.html', datapedidos)



