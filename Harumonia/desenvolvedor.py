class Desenvolvedor:
    def __init__(self, cpf: str, nome: str, valor_hora: float):
        self.__cpf = cpf
        self.__nome = nome
        self.__valor_hora = valor_hora

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def valor_hora(self):
        return self.__valor_hora
    
    @valor_hora.setter
    def valor_hora(self, valor_hora):
        self.__valor_hora = valor_hora