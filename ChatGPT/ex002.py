class Carro:
    def __init__(self, marca: str, modelo: str, velocidade: float = 0):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
    
    def acelerar(self, valor):
        self.velocidade += valor
        print(f"Sua velocidade atual é de {self.velocidade} km/h.")
    
    def frear(self, valor):
        if self.velocidade - valor < 0:
            self.velocidade = 0
        else:
            self.velocidade -= valor
            print(f"Sua velocidade atual é de {self.velocidade} km/h.")

c1 = Carro("Fiat", "Toro")
c1.acelerar(10)
c1.frear(5)
