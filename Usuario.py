class Usuario:
    def __init__(self, id, nombre, correo_electronico, contrasena):
        self._id = id
        self._nombre = nombre
        self._correo_electronico = correo_electronico
        self._contrasena = contrasena

    # Propiedades para manejar los atributos de Usuario

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
    def correo_electronico(self):
        return self._correo_electronico

    @correo_electronico.setter
    def correo_electronico(self, correo):
        self._correo_electronico = correo

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena

    # Método destructor opcional
    def __del__(self):
        print(f"El usuario {self._nombre} ha sido eliminado.")
