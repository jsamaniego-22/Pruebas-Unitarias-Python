# pruebas_patrones.py

from configuracion_sistema import ConfiguracionSistema
from fabrica_entidades import FabricaEntidades
from notificador import Notificador
from interfaz_usuario import InterfazUsuario
from sistema_inventario import SistemaInventario

def prueba_singleton():
    print("\n--- Prueba de Singleton ---")
    config1 = ConfiguracionSistema()
    config2 = ConfiguracionSistema()
    
    config1.establecer_configuracion("modo", "produccion")
    print("Modo en config1:", config1.obtener_configuracion("modo"))
    print("Modo en config2:", config2.obtener_configuracion("modo"))

    print("¿config1 y config2 son la misma instancia?", config1 is config2)

def prueba_factory():
    print("\n--- Prueba de Factory ---")
    # Crear un ProductoDigital y un ProductoFisico
    producto_digital = FabricaEntidades.crear_producto('digital', id=1, nombre="Ebook", descripcion="Libro digital", precio=15.0, stock=50, formato="PDF", tamano_archivo="5MB")
    producto_fisico = FabricaEntidades.crear_producto('fisico', id=2, nombre="Camiseta", descripcion="Camiseta de algodón", precio=20.0, stock=30, peso="200g", dimensiones="M")
    
    # Crear un Cliente y un Administrador
    cliente = FabricaEntidades.crear_usuario('cliente', id=1, nombre="Juan Perez", correo_electronico="juan@example.com", contrasena="securepass")
    administrador = FabricaEntidades.crear_usuario('administrador', id=2, nombre="Ana Admin", correo_electronico="ana@admin.com", contrasena="adminpass")

    # Mostrar detalles de cada instancia
    print("Producto Digital:", producto_digital.mostrar_detalle())
    print("Producto Físico:", producto_fisico.mostrar_detalle())
    print("Cliente:", cliente.nombre, cliente.correo_electronico)
    print("Administrador:", administrador.nombre, administrador.correo_electronico)

def prueba_observer():
    print("\n--- Prueba de Observer ---")
    notificador = Notificador()
    interfaz_usuario = InterfazUsuario()
    sistema_inventario = SistemaInventario()

    # Suscribir observadores
    notificador.suscribir(interfaz_usuario)
    notificador.suscribir(sistema_inventario)

    # Notificar cambios
    notificador.notificar("Se ha actualizado el stock de un producto.")
    notificador.notificar("El estado de un pedido ha cambiado.")

    # Desuscribir y notificar de nuevo
    notificador.desuscribir(interfaz_usuario)
    notificador.notificar("Notificación solo para el sistema de inventario.")

if __name__ == "__main__":
    prueba_singleton()
    prueba_factory()
    prueba_observer()
