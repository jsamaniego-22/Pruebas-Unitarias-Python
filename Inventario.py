# inventario.py

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def actualizar_inventario(self, producto, cantidad):
        if producto.id in self.productos:
            producto.reducir_stock(cantidad)
            print(f"Inventario actualizado: {producto.nombre} - Stock actual: {producto.stock}")
        else:
            print("Producto no encontrado en el inventario")

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(f"{producto.nombre} - Stock: {producto.stock}")
