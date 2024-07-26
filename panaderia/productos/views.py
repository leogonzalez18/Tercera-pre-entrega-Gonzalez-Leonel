from django.shortcuts import render, redirect
from django.contrib import messages
from productos.models import Producto, Categoria, Pedido
from productos.forms import ProductoForm, CategoriaForm, PedidoForm, BuscarProductoForm

def index(request):
    return render(request, 'productos/home.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente.')
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = ProductoForm()
    
    return render(request, 'productos/agregar_producto.html', {'form': form})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría agregada correctamente.')
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CategoriaForm()
    
    return render(request, 'productos/agregar_categoria.html', {'form': form})

def hacer_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido realizado correctamente.')
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = PedidoForm()
    
    return render(request, 'productos/hacer_pedido.html', {'form': form})

def buscar_producto(request):
    formulario = BuscarProductoForm()

    if request.method == 'POST':
        formulario = BuscarProductoForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            productos = Producto.objects.filter(nombre__icontains=info['producto'])
            return render(request, 'productos/lista_productos.html', {'productos': productos, 'formulario': formulario})

    return render(request, 'productos/buscar_producto.html', {'formulario': formulario})