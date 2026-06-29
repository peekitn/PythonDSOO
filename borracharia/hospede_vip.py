from hospede import Hospede

class HospedeVIP(Hospede):
    def __init__(self, percentual_desconto: float, cpf: str, nome: str, telefone: str):
        super().__init__(cpf, nome, telefone)
        self.__percentual_desconto = percentual_desconto

    @property
    def percentual_desconto(self):
        return self.__percentual_desconto
    
    @percentual_desconto.setter
    def percentual_desconto(self, percentual_desconto):
        self.__percentual_desconto = percentual_desconto