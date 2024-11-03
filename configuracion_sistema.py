# configuracion_sistema.py
# Ejemplo de Patron Singleton

class ConfiguracionSistema:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ConfiguracionSistema, cls).__new__(cls)
            cls._instancia.configuraciones = {}
        return cls._instancia

    def obtener_configuracion(self, clave):
        return self.configuraciones.get(clave, None)

    def establecer_configuracion(self, clave, valor):
        self.configuraciones[clave] = valor
