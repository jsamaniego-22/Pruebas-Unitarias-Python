class Producto:
    def __init__(self, id, nombre, descripcion, precio, stock):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._stock = stock

    # Propiedades para acceder y modificar los atributos

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        if precio >= 0:
            self._precio = precio

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        if stock >= 0:
            self._stock = stock
