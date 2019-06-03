from django.db import models
from django.utils import timezone

# Create your models here.

class Cliente(models.Model):
    nome_completo = models.CharField(max_length=30,default=None)
    endereco = models.CharField(max_length=30,default=None)
    numero = models.BigIntegerField(default=None)
    observacao = models.CharField(max_length=30,default=None)
    cep = models.BigIntegerField(default=None)
    bairro = models.CharField(max_length=30, default=None)
    cidade = models.CharField(max_length=30,default=None)
    telefone = models.CharField(max_length=30,default=None)
    email = models.EmailField(max_length=20,default=None)
    def __str__ (self):
        return 'Nome: {}'.format(self.nome_completo)






class Produtos(models.Model):
   descricao_produto = models.CharField( max_length=30)
   preco_produto = models.BigIntegerField(default=None)
   imagem = models.ImageField(upload_to='produto_image')

   def __str__(self):
      return 'Produto: {}'.format(self.descricao_produto)



class Pedidos(models.Model):
   Cliente = models.ForeignKey(
   Cliente, on_delete=models.CASCADE, default=None)
   produto_pedido = models.CharField( max_length=30,blank = True)
   descricao_pedido = models.CharField( max_length=30,default=None)
   quantidade_pedido = models.BigIntegerField(default=None)
   total_pedido = models.BigIntegerField(default=None)
   observacao_pedido = models.CharField( max_length=30)
   data_pedido = models.DateTimeField(default=timezone.now)
   

   def __str__(self):
      return 'Data pedido: {}, descricao_pedido {} '.format(self.data_pedido, self.descricao_pedido)