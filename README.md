## Tercera-pre-entrega-Gonzalez-Leonel - Panadería 
Este proyecto es una aplicación web para una panadería, que permite la gestión de productos, categorías y pedidos.
Los usuarios pueden agregar productos y categorías, buscar productos y realizar pedidos.

## Instalación

1. **Crear un entorno virtual**

2. **Activar el entorno virtual**

3. **Instalar las dependencias**
   
   Navegar al directorio `Tercera-pre-entrega-Gonzalez-Leonel` y ejecuta:
   
   ```bash
   pipenv install -r requirements.txt
   ```

4. **Iniciar el servidor de desarrollo**
   
   Navegar al directorio `Tercera-pre-entrega-Gonzalez-Leonel/panaderia` y ejecuta:
   ```bash
   python manage.py runserver
   ```

## Uso

Abri tu navegador y accede a http://127.0.0.1:8000/ para ver la aplicación.

Agregar Producto:
Navega a http://127.0.0.1:8000/agregar-producto/ y completa el formulario para agregar un producto.

Agregar Categoría:
Navega a http://127.0.0.1:8000/agregar-categoria/ y completa el formulario para agregar una categoría.

Hacer Pedido:
Navega a http://127.0.0.1:8000/hacer-pedido/ y completa el formulario para realizar un pedido.

Buscar Producto:
Navega a http://127.0.0.1:8000/buscar-producto/ y utiliza el formulario para buscar productos en la base de datos.