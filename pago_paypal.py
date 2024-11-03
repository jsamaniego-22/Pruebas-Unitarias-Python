# pago_paypal.py

from proceso_pago import ProcesoPago

class PagoPayPal(ProcesoPago):
    def iniciar_pago(self, monto):
        print(f"Iniciando pago con PayPal por {monto}...")
        return True

    def verificar_pago(self):
        print("Verificando pago con PayPal...")
        return True

    def confirmar_pago(self):
        print("Pago con PayPal confirmado.")
        return True
