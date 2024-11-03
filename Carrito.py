# carrito.py

from Producto import Producto

class Carrito:
    def __init__(self):
        self._productos = []
        self._total = 0.0

    @property
    def total(self):
        return self._total

    def agregar_producto(self, producto, cantidad=1):
        if isinstance(producto, Producto) and cantidad > 0:
            self._productos.append((producto, cantidad))
            producto.reducir_stock(cantidad)
            self.calcular_total()
        else:
            raise ValueError("Producto inválido o cantidad no válida")

    def calcular_total(self):
        self._total = sum(prod.precio * cant for prod, cant in self._productos)

    def mostrar_carrito(self):
        for producto, cantidad in self._productos:
            print(f"{producto.nombre} - Cantidad: {cantidad} - Precio Total: {producto.precio * cantidad}")
        print(f"Total del Carrito: {self._total}")
