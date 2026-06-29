from cliente import Cliente

class ClienteInvestidor(Cliente):
    def __init__(self, percentual_cashback: float, cpf: str, nome: str, telefone: str):
        super().__init__(cpf, nome, telefone)
        self.__percentual_cashback = percentual_cashback

    @property
    def percentual_cashback(self):
        return self.__percentual_cashback
    
    @percentual_cashback.setter
    def percentual_cashback(self, percentual_cashback):
        self.__percentual_cashback = percentual_cashback