class cuentabancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print("depósito de", monto, "realizado nuevo balance", self.balance)
        else:
            print("el monto a depositar debe ser positivo")

    def retirar(self, monto):
        if 0 < monto <= self.balance:
            self.balance -= monto
            print("retiro de", monto, "realizado nuevo balance", self.balance)
        else:
            print("monto inválido para retirar")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print("Se aplicó una cuota de manejo de", cuota, "Nuevo balance", self.balance)

    def mostrar_detalles(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print("Propietarios" .join(self.propietarios))
        print("Balance", self.balance)


cuenta = cuentabancaria("2334445555", ["Cristian Lucio, Michell Gil"], 1000)
cuenta.mostrar_detalles()
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.aplicar_cuota_manejo()
cuenta.mostrar_detalles()
