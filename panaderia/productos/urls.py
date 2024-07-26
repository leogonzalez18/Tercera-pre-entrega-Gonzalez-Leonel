from django.urls import path, include
from productos import views

urlpatterns = [
    path('', views.index, name='home'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('buscar-producto/', views.buscar_producto, name='buscar_producto'),
    path('hacer-pedido/', views.hacer_pedido, name='hacer_pedido'),
    path('agregar-categoria/', views.agregar_categoria, name='agregar_categoria'),
]
