class Cliente:
    def __init__(self, cpf: str, nome: str, cnh: str):
        self.__cpf = cpf
        self.__nome = nome
        self.__cnh = cnh
    
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
    def cnh(self):
        return self.__cnh
    
    @cnh.setter
    def cnh(self, cnh):
        self.__cnh = cnh