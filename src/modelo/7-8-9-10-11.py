class Cuenta_Bancaria:
    def __init__(self,numero_cuenta, propietarios,balance, propietarios ):
        self.numero_cuenta= numero_cuenta
        self.propietarios= propietarios
        self.balance= balance

    def depositar(self, acciones):
        self.balance += acciones 
        print("se aumento las acciones", acciones)

    def retiro(self, acciones):
        if acciones <= self.balance:
            self.balance -= acciones 
            print("se retiraron", acciones)
    
    def aplicar_cuota_manejo(self):
        cuota=self.balance*0.02
        self.balance -= cuota
        print("cuota de manejo aplicada", cuota)

    def detalles (self):
        print("numero de cuenta:", self.numero_cuenta)
        print(f"Propietarios: {", ".join(self.propietarios)}")
        print("balAnce: ", self.balance)