# main.py

from Producto import Producto
from Usuario import Usuario
from Carrito import Carrito

def prueba_producto():
    print("\n--- Prueba de la Clase Producto ---")
    producto = Producto(id=1, nombre="Laptop", descripcion="Laptop de 15 pulgadas", precio=1000.0, stock=10)
    
    # Acceso a propiedades
    print(f"Producto: {producto.nombre} - Precio: {producto.precio} - Stock: {producto.stock}")
    
    # Modificación de propiedades
    producto.precio = 950.0
    producto.stock = 8
    print(f"Producto Actualizado: {producto.nombre} - Precio: {producto.precio} - Stock: {producto.stock}")

def prueba_usuario():
    print("\n--- Prueba de la Clase Usuario ---")
    usuario = Usuario(id=1, nombre="Juan Perez", correo_electronico="juan@example.com", contrasena="securepassword")
    
    # Acceso a propiedades
    print(f"Usuario: {usuario.nombre} - Correo: {usuario.correo_electronico}")
    
    # Modificación de propiedades
    usuario.nombre = "Juan P."
    usuario.correo_electronico = "juanp@example.com"
    print(f"Usuario Actualizado: {usuario.nombre} - Correo: {usuario.correo_electronico}")

def prueba_carrito():
    print("\n--- Prueba de la Clase Carrito ---")
    
    # Crear productos
    producto1 = Producto(id=1, nombre="Laptop", descripcion="Laptop de 15 pulgadas", precio=1000.0, stock=5)
    producto2 = Producto(id=2, nombre="Mouse", descripcion="Mouse inalámbrico", precio=50.0, stock=10)
    
    # Crear carrito y agregar productos
    carrito = Carrito()
    carrito.agregar_producto(producto1, 2)
    carrito.agregar_producto(producto2, 3)
    
    # Verificar el contenido del carrito
    carrito.mostrar_carrito()
    
    # Remover un producto y verificar el total actualizado
    carrito.remover_producto(producto2)
    carrito.mostrar_carrito()

if __name__ == "__main__":
    prueba_producto()
    prueba_usuario()
    prueba_carrito()
