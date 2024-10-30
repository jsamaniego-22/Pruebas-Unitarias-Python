# pruebas_polimorfismo.py

from Producto import ProductoDigital, ProductoFisico
from Carrito import Carrito
from Inventario import Inventario

def prueba_polimorfismo():
    print("\n--- Prueba de Polimorfismo en Inventario ---")
    inventario = Inventario()
    prod_digital = ProductoDigital(id=1, nombre="Ebook", descripcion="Libro digital en PDF", precio=10.0, stock=100, formato="PDF", tamano_archivo="5MB")
    prod_fisico = ProductoFisico(id=2, nombre="Camiseta", descripcion="Camiseta de algodón", precio=20.0, stock=50, peso="200g", dimensiones="M")
    
    inventario.agregar_producto(prod_digital)
    inventario.agregar_producto(prod_fisico)
    
    inventario.mostrar_inventario()

def prueba_sobrecarga():
    print("\n--- Prueba de Sobrecarga en Carrito ---")
    carrito = Carrito()
    inventario = Inventario()
    ebook = ProductoDigital(id=1, nombre="Ebook", descripcion="Libro digital en PDF", precio=10.0, stock=100, formato="PDF", tamano_archivo="5MB")
    camiseta = ProductoFisico(id=2, nombre="Camiseta", descripcion="Camiseta de algodón", precio=20.0, stock=50, peso="200g", dimensiones="M")

    # Agregar productos al inventario para luego buscarlos por ID
    inventario.agregar_producto(ebook)
    inventario.agregar_producto(camiseta)

    # Agregar productos usando diferentes argumentos
    carrito.agregar_producto(producto=ebook, cantidad=2)
    carrito.agregar_producto(id=2, cantidad=3, inventario=inventario)
    carrito.agregar_producto(nombre="Producto Genérico", precio=15.0, cantidad=1)

    carrito.mostrar_carrito()

def prueba_sobreescritura():
    print("\n--- Prueba de Sobreescritura de Métodos ---")
    ebook = ProductoDigital(id=1, nombre="Ebook", descripcion="Libro digital en PDF", precio=10.0, stock=100, formato="PDF", tamano_archivo="5MB")
    camiseta = ProductoFisico(id=2, nombre="Camiseta", descripcion="Camiseta de algodón", precio=20.0, stock=50, peso="200g", dimensiones="M")

    # Mostrar detalles específicos de cada tipo de producto
    print(ebook.mostrar_detalle())
    print(camiseta.mostrar_detalle())

if __name__ == "__main__":
    prueba_polimorfismo()
    prueba_sobrecarga()
    prueba_sobreescritura()
