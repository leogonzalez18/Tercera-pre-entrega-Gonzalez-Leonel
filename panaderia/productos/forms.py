from django import forms
from productos.models import Producto, Categoria, Pedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class BuscarProductoForm(forms.Form):
    producto = forms.CharField(label='Buscar Producto', max_length=100)