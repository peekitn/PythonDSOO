class Bagagem:
    def __init__(self, codigo: int, peso: float, preco_extra: float):
        self.__codigo = codigo
        self.__peso = peso
        self.__preco_extra = preco_extra

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def preco_extra(self):
        return self.__preco_extra
    
    @preco_extra.setter
    def preco_extra(self, preco_extra):
        self.__preco_extra = preco_extra

    