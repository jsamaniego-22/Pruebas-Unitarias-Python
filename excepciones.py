# excepciones.py

class InventarioInsuficienteExcepcion(Exception):
    def __init__(self, mensaje="Stock insuficiente para completar la operación."):
        super().__init__(mensaje)

class PagoFallidoExcepcion(Exception):
    def __init__(self, mensaje="El pago ha fallado. Verifique sus datos e inténtelo nuevamente."):
        super().__init__(mensaje)

class UsuarioNoAutorizadoExcepcion(Exception):
    def __init__(self, mensaje="Usuario no autorizado para realizar esta operación."):
        super().__init__(mensaje)
