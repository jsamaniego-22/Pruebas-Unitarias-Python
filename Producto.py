# producto.py

class Producto:
    def __init__(self, id, nombre, descripcion, precio, stock):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._stock = stock

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock

    def reducir_stock(self, cantidad):
        if cantidad <= self._stock:
            self._stock -= cantidad
        else:
            print("Stock insuficiente")

class ProductoDigital(Producto):
    def __init__(self, id, nombre, descripcion, precio, stock, formato, tamano_archivo):
        super().__init__(id, nombre, descripcion, precio, stock)
        self.formato = formato
        self.tamano_archivo = tamano_archivo

class ProductoFisico(Producto):
    def __init__(self, id, nombre, descripcion, precio, stock, peso, dimensiones):
        super().__init__(id, nombre, descripcion, precio, stock)
        self.peso = peso
        self.dimensiones = dimensiones
