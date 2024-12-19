# test_plataforma.py

import unittest
from Producto import ProductoDigital
from excepciones import InventarioInsuficienteExcepcion, PagoFallidoExcepcion
from pago_tarjeta import PagoTarjeta

class TestProducto(unittest.TestCase):
    def setUp(self):
        # Cambiar a una subclase concreta
        self.producto = ProductoDigital(
            id=1,
            nombre="Ebook",
            descripcion="Libro digital",
            precio=15.0,
            stock=10,
            formato="PDF",
            tamano_archivo="5MB"
        )

    def test_reducir_stock_exitoso(self):
        self.producto.reducir_stock(15)
        self.assertEqual(self.producto.stock, 5)

    def test_reducir_stock_insuficiente(self):
        with self.assertRaises(InventarioInsuficienteExcepcion):
            self.producto.reducir_stock(15)

    def test_stock_no_negativo(self):
        with self.assertRaises(ValueError):
            self.producto.stock = -1


if __name__ == '__main__':
    unittest.main()
