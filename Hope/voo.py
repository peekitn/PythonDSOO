class Voo:
    def __init__(self, numero: str, origem: str, destino: str, preco_base: float):
        self.__numero = numero
        self.__origem = origem
        self.__destino = destino
        self.__preco_base = preco_base

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def origem(self):
        return self.__origem
    
    @origem.setter
    def origem(self, origem):
        self.__origem = origem
    
    @property
    def destino(self):
        return self.__destino
    
    @destino.setter
    def destino(self, destino):
        self.__destino = destino

    @property
    def preco_base(self):
        return self.__preco_base
    
    @preco_base.setter
    def preco_base(self, preco_base):
        self.__preco_base = preco_base