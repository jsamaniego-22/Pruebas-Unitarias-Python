# pruebas_abst_inter.py

from inventario_digital import InventarioDigital
from inventario_fisico import InventarioFisico
from pago_tarjeta import PagoTarjeta
from pago_paypal import PagoPayPal
from Producto import ProductoDigital, ProductoFisico

def prueba_gestion_inventario():
    print("\n--- Prueba de Gestión de Inventario ---")
    
    # Crear productos
    ebook = ProductoDigital(id=1, nombre="Ebook", descripcion="Libro digital", precio=15.0, stock=50, formato="PDF", tamano_archivo="5MB")
    camiseta = ProductoFisico(id=2, nombre="Camiseta", descripcion="Camiseta de algodón", precio=20.0, stock=30, peso="200g", dimensiones="M")

    # Crear instancias de inventarios y añadir productos
    inventario_digital = InventarioDigital()
    inventario_fisico = InventarioFisico()

    inventario_digital.añadir_producto(ebook)
    inventario_fisico.añadir_producto(camiseta)

    # Actualizar stock
    inventario_digital.actualizar_stock(ebook.id, 10)
    inventario_fisico.actualizar_stock(camiseta.id, -5)

    # Eliminar producto
    inventario_digital.eliminar_producto(ebook.id)
    inventario_fisico.eliminar_producto(camiseta.id)

def prueba_proceso_pago():
    print("\n--- Prueba de Procesos de Pago ---")
    
    # Crear instancias de métodos de pago
    pago_tarjeta = PagoTarjeta()
    pago_paypal = PagoPayPal()

    # Probar pago con tarjeta
    if pago_tarjeta.iniciar_pago(100):
        if pago_tarjeta.verificar_pago():
            pago_tarjeta.confirmar_pago()

    # Probar pago con PayPal
    if pago_paypal.iniciar_pago(50):
        if pago_paypal.verificar_pago():
            pago_paypal.confirmar_pago()

if __name__ == "__main__":
    prueba_gestion_inventario()
    prueba_proceso_pago()
