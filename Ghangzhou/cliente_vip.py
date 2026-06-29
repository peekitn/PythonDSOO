from cliente import Cliente

class ClienteVip(Cliente):
    def __init__(self, bonus_rendimento: float, cpf: str, nome: str, telefone: str):
        super().__init__(cpf, nome, telefone)
        self.__bonus_rendimento = bonus_rendimento

    @property
    def bonus_rendimento(self):
        return self.__bonus_rendimento
    
    @bonus_rendimento.setter
    def bonus_rendimento(self, bonus_rendimento):
        self.__bonus_rendimento = bonus_rendimento

    