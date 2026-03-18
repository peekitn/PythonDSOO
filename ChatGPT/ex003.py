class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado.")
        
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado.")
    
    def ver_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

# Teste
c1 = ContaBancaria("Lucas", 100)
c1.depositar(50)
c1.sacar(30)
c1.ver_saldo()
