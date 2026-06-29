from cliente import Cliente

class ClienteCorporativo(Cliente):
    def __init__(self, percentual_desconto: float, cpf: str, nome: str, cnh: str):
        super().__init__(cpf, nome, cnh)
        self.__percentual_desconto = percentual_desconto

    @property
    def percentual_desconto(self):
        return self.__percentual_desconto
    
    @percentual_desconto.setter
    def percentual_desconto(self, percentual_desconto):
        self.__percentual_desconto = percentual_desconto