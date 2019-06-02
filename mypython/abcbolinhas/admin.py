from django.contrib import admin
from  .models import Cliente
from  .models import Produtos
from  .models import Pedidos
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Produtos)
admin.site.register(Pedidos)