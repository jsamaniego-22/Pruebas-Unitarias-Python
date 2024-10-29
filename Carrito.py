class Carrito:
    def __init__(self):
        self._productos = []  # Lista de productos en el carrito
        self._total = 0.0     # Total del carrito

    # Método para agregar productos al carrito
    def agregar_producto(self, producto, cantidad=1):
        if producto.stock >= cantidad:
            self._productos.append((producto, cantidad))
            producto.stock -= cantidad  # Reducir stock del producto
            self.calcular_total()
        else:
            print("No hay suficiente stock para añadir este producto.")

    # Método para remover productos del carrito
    def remover_producto(self, producto):
        for p, cantidad in self._productos:
            if p.id == producto.id:
                self._productos.remove((p, cantidad))
                p.stock += cantidad  # Devolver stock al inventario
                self.calcular_total()
                break

    # Método para calcular el total del carrito
    def calcular_total(self):
        self._total = sum(producto.precio * cantidad for producto, cantidad in self._productos)

    @property
    def total(self):
        return self._total

    # Método para mostrar productos en el carrito
    def mostrar_carrito(self):
        for producto, cantidad in self._productos:
            print(f"{producto.nombre} - Cantidad: {cantidad} - Precio Total: {producto.precio * cantidad}")
        print(f"Total del Carrito: {self._total}")
