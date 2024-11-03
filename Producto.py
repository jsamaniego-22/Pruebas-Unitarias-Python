# producto.py

from item import Item

class Producto(Item):
    def __init__(self, id, nombre, descripcion, precio, stock):
        super().__init__(id, nombre, precio)
        self._descripcion = descripcion
        self._stock = stock

    # Accesor y mutador para stock
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        if stock >= 0:
            self._stock = stock
        else:
            raise ValueError("El stock no puede ser negativo")

    # Accesor y mutador para descripción
    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        if isinstance(descripcion, str):
            self._descripcion = descripcion
        else:
            raise ValueError("Descripción no válida")

    # Método para reducir el stock
    def reducir_stock(self, cantidad):
        if cantidad > self._stock:
            print("Stock insuficiente para reducir")
        else:
            self._stock -= cantidad
            print(f"Stock de {self._nombre} reducido en {cantidad}. Stock actual: {self._stock}")


# ProductoDigital y ProductoFisico en producto.py

class ProductoDigital(Producto):
    def __init__(self, id, nombre, descripcion, precio, stock, formato, tamano_archivo):
        super().__init__(id, nombre, descripcion, precio, stock)
        self._formato = formato
        self._tamano_archivo = tamano_archivo

    @property
    def formato(self):
        return self._formato

    @property
    def tamano_archivo(self):
        return self._tamano_archivo

    def mostrar_detalle(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Formato: {self.formato}, Tamaño: {self.tamano_archivo}"


class ProductoFisico(Producto):
    def __init__(self, id, nombre, descripcion, precio, stock, peso, dimensiones):
        super().__init__(id, nombre, descripcion, precio, stock)
        self._peso = peso
        self._dimensiones = dimensiones

    @property
    def peso(self):
        return self._peso

    @property
    def dimensiones(self):
        return self._dimensiones

    def mostrar_detalle(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Peso: {self.peso}, Dimensiones: {self.dimensiones}"
