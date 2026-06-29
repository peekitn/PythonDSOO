from paciente import Paciente

class PacientePlanoSaude(Paciente):
    def __init__(self, numero_carteirinha: str, percentual_desconto: float, cpf: str, nome: str, idade: int):
        super().__init__(cpf, nome, idade)
        self.__numero_carteirinha = numero_carteirinha
        self.__percentual_desconto = percentual_desconto
        
    @property
    def numero_carteirinha(self):
        return self.__numero_carteirinha
    
    @numero_carteirinha.setter
    def numero_carteirinha(self, numero_carteirinha):
        self.__numero_carteirinha = numero_carteirinha

    @property
    def percentual_desconto(self):
        return self.__percentual_desconto
    
    @percentual_desconto.setter
    def percentual_desconto(self, percentual_desconto):
        self.__percentual_desconto = percentual_desconto