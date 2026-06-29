class Professor:
    def __init__(self, registro: int, nome: str):
        self.__registro = registro
        self.__nome = nome

    @property
    def registro(self):
        return self.__registro
    
    @registro.setter
    def registro(self, registro):
        self.__registro = registro

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome