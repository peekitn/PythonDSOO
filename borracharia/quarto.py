class Quarto:
    def __init__(self, numero: int, tipo: str, valor_diaria: float):
        self.__numero = numero
        self.__tipo = tipo
        self.__valor_diaria = valor_diaria

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def valor_diaria(self):
        return self.__valor_diaria
    
    @valor_diaria.setter
    def valor_diaria(self, valor_diaria):
        self.__valor_diaria = valor_diaria