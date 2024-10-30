# Carrito.py

from Producto import Producto  # Asegúrate de que la ruta y el nombre del archivo sean correctos

class Carrito:
    def __init__(self):
        self._productos = []
        self._total = 0.0

    # Sobrecarga simulada del método agregar_producto
    def agregar_producto(self, producto=None, id=None, nombre=None, precio=None, cantidad=1, inventario=None):
        if producto is not None:
            # Agregar producto por objeto Producto
            self._productos.append((producto, cantidad))
            producto.reducir_stock(cantidad)
        elif id is not None and inventario is not None:
            # Buscar y agregar producto por ID usando el inventario
            prod = inventario.obtener_producto_por_id(id)
            if prod:
                self._productos.append((prod, cantidad))
                prod.reducir_stock(cantidad)
        elif nombre is not None and precio is not None:
            # Agregar producto directamente por nombre y precio
            self._productos.append((Producto(None, nombre, "", precio, 0), cantidad))
        
        self.calcular_total()

    def calcular_total(self):
        self._total = sum(producto.precio * cantidad for producto, cantidad in self._productos)

    def mostrar_carrito(self):
        for producto, cantidad in self._productos:
            print(f"{producto.nombre} - Cantidad: {cantidad} - Precio Total: {producto.precio * cantidad}")
        print(f"Total del Carrito: {self._total}")
