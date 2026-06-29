from passageiro import Passageiro

class PassageiroFrequente(Passageiro):
    def __init__(self, milhas_acumuladas: int, desconto: float, cpf: str, nome: str, telefone: str):
        super().__init__(cpf, nome, telefone)
        self.__milhas_acumuladas = milhas_acumuladas
        self.__desconto = desconto

    @property
    def milhas_acumuladas(self):
        return self.__milhas_acumuladas
    
    @milhas_acumuladas.setter
    def milhas_acumuladas(self, milhas_acumuladas):
        self.__milhas_acumuladas = milhas_acumuladas

    @property
    def desconto(self):
        return self.__desconto
    
    @desconto.setter
    def desconto(self, desconto):
        self.__desconto = desconto