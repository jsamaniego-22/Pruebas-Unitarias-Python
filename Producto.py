# producto.py

# Producto.py

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
    def precio(self):
        return self._precio

    @property
    def nombre(self):
        return self._nombre

    @property
    def stock(self):
        return self._stock

    # Método para reducir el stock
    def reducir_stock(self, cantidad):
        if cantidad > self._stock:
            print("Stock insuficiente para reducir")
        else:
            self._stock -= cantidad
            print(f"Stock de {self._nombre} reducido en {cantidad}. Stock actual: {self._stock}")

    def mostrar_detalle(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Precio: {self._precio}, Stock: {self._stock}"

class ProductoDigital(Producto):
    def __init__(self, id, nombre, descripcion, precio, stock, formato, tamano_archivo):
        super().__init__(id, nombre, descripcion, precio, stock)
        self.formato = formato
        self.tamano_archivo = tamano_archivo

    # Sobreescritura del método mostrar_detalle
    def mostrar_detalle(self):
        return super().mostrar_detalle() + f", Formato: {self.formato}, Tamaño: {self.tamano_archivo}"


class ProductoFisico(Producto):
    def __init__(self, id, nombre, descripcion, precio, stock, peso, dimensiones):
        super().__init__(id, nombre, descripcion, precio, stock)
        self.peso = peso
        self.dimensiones = dimensiones

    # Sobreescritura del método mostrar_detalle
    def mostrar_detalle(self):
        return super().mostrar_detalle() + f", Peso: {self.peso}, Dimensiones: {self.dimensiones}"
