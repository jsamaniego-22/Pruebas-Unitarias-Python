# pruebas.py

from Producto import ProductoDigital, ProductoFisico
from Usuario import Cliente, Administrador
from Inventario import Inventario

def prueba_productos():
    print("\n--- Prueba de Productos Digitales y Físicos ---")
    prod_digital = ProductoDigital(id=1, nombre="Ebook", descripcion="Libro digital en PDF", precio=10.0, stock=100, formato="PDF", tamano_archivo="5MB")
    prod_fisico = ProductoFisico(id=2, nombre="Camiseta", descripcion="Camiseta de algodón", precio=20.0, stock=50, peso="200g", dimensiones="M")

    print(f"Producto Digital: {prod_digital.nombre} - Formato: {prod_digital.formato} - Tamaño: {prod_digital.tamano_archivo}")
    print(f"Producto Físico: {prod_fisico.nombre} - Peso: {prod_fisico.peso} - Dimensiones: {prod_fisico.dimensiones}")

def prueba_usuarios():
    print("\n--- Prueba de Clientes y Administradores ---")
    cliente = Cliente(id=1, nombre="Juan Pérez", correo_electronico="juan@example.com", contrasena="securepassword")
    admin = Administrador(id=2, nombre="Ana Martínez", correo_electronico="ana@example.com", contrasena="adminpassword")

    print(f"Cliente: {cliente.nombre} - Correo: {cliente.correo_electronico}")
    print(f"Administrador: {admin.nombre} - Correo: {admin.correo_electronico}")

    # Cliente compra un producto
    ebook = ProductoDigital(id=3, nombre="Ebook", descripcion="Libro digital en PDF", precio=10.0, stock=100, formato="PDF", tamano_archivo="5MB")
    cliente.agregar_a_historial(ebook)
    print(f"Historial de Compras del Cliente: {[p.nombre for p in cliente.historial_compras]}")

def prueba_inventario():
    print("\n--- Prueba de Inventario ---")
    inventario = Inventario()
    ebook = ProductoDigital(id=1, nombre="Ebook", descripcion="Libro digital en PDF", precio=10.0, stock=100, formato="PDF", tamano_archivo="5MB")
    camiseta = ProductoFisico(id=2, nombre="Camiseta", descripcion="Camiseta de algodón", precio=20.0, stock=50, peso="200g", dimensiones="M")

    # Agregar productos al inventario
    inventario.agregar_producto(ebook)
    inventario.agregar_producto(camiseta)

    # Mostrar inventario
    inventario.mostrar_inventario()

    # Administrador actualiza el inventario
    admin = Administrador(id=3, nombre="Ana Martínez", correo_electronico="ana@example.com", contrasena="adminpassword")
    admin.gestionar_inventario(inventario, ebook, 10)  # Reducción de stock
    inventario.mostrar_inventario()

if __name__ == "__main__":
    prueba_productos()
    prueba_usuarios()
    prueba_inventario()
