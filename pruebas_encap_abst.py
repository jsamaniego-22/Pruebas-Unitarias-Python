# pruebas_encap_abst.py

from Producto import ProductoDigital, ProductoFisico
from Usuario import Usuario
from Carrito import Carrito
from Inventario import Inventario

def prueba_encapsulamiento_producto():
    print("\n--- Prueba de Encapsulamiento en Producto ---")
    
    # Crear instancia de ProductoDigital
    ebook = ProductoDigital(id=1, nombre="Ebook", descripcion="Libro digital en PDF", precio=15.0, stock=50, formato="PDF", tamano_archivo="5MB")

    # Acceder y modificar atributos a través de propiedades
    print("Precio original:", ebook.precio)
    ebook.precio = 20.0
    print("Precio actualizado:", ebook.precio)
    
    # Intentar establecer un precio negativo
    try:
        ebook.precio = -10.0
    except ValueError as e:
        print("Error al establecer precio:", e)
    
    # Verificar stock y reducirlo
    print("Stock original:", ebook.stock)
    ebook.reducir_stock(5)
    print("Stock después de reducir:", ebook.stock)

def prueba_encapsulamiento_usuario():
    print("\n--- Prueba de Encapsulamiento en Usuario ---")
    
    # Crear instancia de Usuario con un correo válido
    usuario = Usuario(id=1, nombre="Juan Perez", correo_electronico="juan@example.com", contrasena="securepass")
    print("Correo original:", usuario.correo_electronico)

    # Intentar establecer un correo inválido
    try:
        usuario.correo_electronico = "correo_invalido"
    except ValueError as e:
        print("Error al establecer correo:", e)
    
    # Intentar establecer una contraseña demasiado corta
    try:
        usuario.contrasena = "123"
    except ValueError as e:
        print("Error al establecer contraseña:", e)

def prueba_abstraccion_item():
    print("\n--- Prueba de Abstracción con Clase Item ---")
    
    # Crear instancias de ProductoDigital y ProductoFisico
    ebook = ProductoDigital(id=2, nombre="Ebook", descripcion="Libro digital en formato PDF", precio=12.0, stock=100, formato="PDF", tamano_archivo="5MB")
    camiseta = ProductoFisico(id=3, nombre="Camiseta", descripcion="Camiseta de algodón", precio=25.0, stock=20, peso="200g", dimensiones="M")

    # Usar el método mostrar_detalle, que está definido en Item
    print(ebook.mostrar_detalle())
    print(camiseta.mostrar_detalle())

def prueba_encapsulamiento_carrito():
    print("\n--- Prueba de Encapsulamiento en Carrito ---")
    
    # Crear instancias de productos y carrito
    carrito = Carrito()
    inventario = Inventario()

    ebook = ProductoDigital(id=1, nombre="Ebook", descripcion="Libro digital en PDF", precio=10.0, stock=50, formato="PDF", tamano_archivo="5MB")
    camiseta = ProductoFisico(id=2, nombre="Camiseta", descripcion="Camiseta de algodón", precio=20.0, stock=30, peso="200g", dimensiones="M")

    # Agregar productos al inventario y al carrito
    inventario.agregar_producto(ebook)
    inventario.agregar_producto(camiseta)
    
    # Agregar productos al carrito y verificar total
    carrito.agregar_producto(ebook, cantidad=2)
    carrito.agregar_producto(camiseta, cantidad=3)

    # Mostrar el contenido y total del carrito
    carrito.mostrar_carrito()

    # Intentar agregar un producto con cantidad inválida
    try:
        carrito.agregar_producto(camiseta, cantidad=-1)
    except ValueError as e:
        print("Error al agregar producto con cantidad inválida:", e)

if __name__ == "__main__":
    prueba_encapsulamiento_producto()
    prueba_encapsulamiento_usuario()
    prueba_abstraccion_item()
    prueba_encapsulamiento_carrito()
