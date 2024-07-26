#superuser username: admin password: admin 

from django.contrib import admin
from productos.models import Producto, Categoria, Pedido

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Pedido)
