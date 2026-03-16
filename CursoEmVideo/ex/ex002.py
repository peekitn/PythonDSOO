# Declaracao de Classes
class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depositos
    """
    def __init__(self, id, titular, saldo = 0):
        # Atributos de Instancia
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R$ {self.saldo:.2f}")
        #Metodos de Instancia
    def __str__(self):
        return f"A conta {self.id} de  {self.titular} tem {self.saldo:.2f} de saldo"
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque NEGADO de R${valor:.2f} na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} autorizado na conta {self.id}")

# Declaracao de Objetos
c1 = ContaBancaria(id = 112, titular = "Gustavo", saldo = 3000)
c1.depositar(500)
c1.sacar(5000)
print(c1)